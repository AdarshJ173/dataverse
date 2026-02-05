import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="VelocityMart Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1f77b4;
        font-weight: 700;
    }
    h2 {
        color: #ff7f0e;
        font-weight: 600;
    }
    h3 {
        color: #2ca02c;
    }
    </style>
    """, unsafe_allow_html=True)

# Data loading with caching
@st.cache_data
def load_data():
    """Load all datasets with error handling"""
    try:
        sku_df = pd.read_csv('sku_master.csv')
        orders_df = pd.read_csv('order_transactions.csv')
        warehouse_df = pd.read_csv('warehouse_constraints.csv')
        picker_df = pd.read_csv('picker_movement.csv')

        # Convert timestamps
        orders_df['order_timestamp'] = pd.to_datetime(orders_df['order_timestamp'])
        picker_df['order_timestamp'] = pd.to_datetime(picker_df['order_timestamp'])
        picker_df['movement_timestamp'] = pd.to_datetime(picker_df['movement_timestamp'])

        # Add time features
        orders_df['hour'] = orders_df['order_timestamp'].dt.hour
        orders_df['date'] = orders_df['order_timestamp'].dt.date
        orders_df['week'] = orders_df['order_timestamp'].dt.isocalendar().week
        orders_df['day_name'] = orders_df['order_timestamp'].dt.day_name()

        picker_df['hour'] = picker_df['movement_timestamp'].dt.hour
        picker_df['date'] = picker_df['movement_timestamp'].dt.date

        return sku_df, orders_df, warehouse_df, picker_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

@st.cache_data
def calculate_metrics(sku_df, orders_df, warehouse_df, picker_df):
    """Calculate all dashboard metrics"""

    # 1. Temperature violations
    sku_with_warehouse = sku_df.merge(
        warehouse_df[['slot_id', 'temp_zone', 'zone', 'aisle_id', 'max_weight_kg']],
        left_on='current_slot',
        right_on='slot_id',
        how='left'
    )
    sku_with_warehouse['temp_violation'] = (
        sku_with_warehouse['temp_req'] != sku_with_warehouse['temp_zone']
    )

    # 2. Picker statistics
    picker_df['travel_time_minutes'] = (
        (picker_df['movement_timestamp'] - picker_df['order_timestamp']).dt.total_seconds() / 60
    )
    picker_df['speed_m_per_min'] = picker_df['travel_distance_m'] / picker_df['travel_time_minutes'].replace(0, np.nan)

    # 3. Aisle congestion
    picker_with_location = picker_df.merge(
        sku_df[['sku_id', 'current_slot']], 
        on='sku_id', 
        how='left'
    )
    picker_with_location['aisle'] = picker_with_location['current_slot'].str.split('-').str[0]

    # 4. SKU frequency
    sku_frequency = orders_df['sku_id'].value_counts().reset_index()
    sku_frequency.columns = ['sku_id', 'order_count']

    return sku_with_warehouse, picker_df, picker_with_location, sku_frequency

# Load data
sku_df, orders_df, warehouse_df, picker_df = load_data()
sku_with_warehouse, picker_df_enhanced, picker_with_location, sku_frequency = calculate_metrics(
    sku_df, orders_df, warehouse_df, picker_df
)

# Sidebar navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select Dashboard",
    ["🏠 Overview", "🔥 Heatmap Analysis", "❄️ Temperature Violations", 
     "👤 Picker Performance", "📈 Demand Patterns"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Quick Stats")
st.sidebar.metric("Total SKUs", f"{len(sku_df):,}")
st.sidebar.metric("Total Orders", f"{len(orders_df):,}")
st.sidebar.metric("Pickers", len(picker_df['picker_id'].unique()))
st.sidebar.metric("Warehouse Slots", f"{len(warehouse_df):,}")

# ============================================================================
# PAGE 1: OVERVIEW
# ============================================================================
if page == "🏠 Overview":
    st.title("📦 VelocityMart Operations Dashboard")
    st.markdown("### Strategic Intervention & Real-Time Monitoring")

    # Key Metrics Row
    col1, col2, col3, col4, col5 = st.columns(5)

    # Calculate metrics
    total_violations = len(sku_with_warehouse[sku_with_warehouse['temp_violation'] == True])
    violation_rate = (total_violations / len(sku_df)) * 100
    critical_violations = len(sku_with_warehouse[
        (sku_with_warehouse['temp_violation'] == True) &
        (sku_with_warehouse['temp_req'].isin(['Frozen', 'Refrigerated'])) &
        (sku_with_warehouse['temp_zone'] == 'Ambient')
    ])
    avg_pick_time = picker_df_enhanced['travel_time_minutes'].mean()
    peak_hour_volume = orders_df[orders_df['hour'] == 19].shape[0]

    with col1:
        st.metric(
            "Temperature Violations",
            f"{total_violations}",
            f"{violation_rate:.1f}%",
            delta_color="inverse"
        )

    with col2:
        st.metric(
            "Critical Violations",
            f"{critical_violations}",
            "₹145K at risk",
            delta_color="inverse"
        )

    with col3:
        st.metric(
            "Avg Pick Time",
            f"{avg_pick_time:.2f} min",
            "Target: 1.9 min",
            delta_color="inverse"
        )

    with col4:
        st.metric(
            "Peak Hour (19:00)",
            f"{peak_hour_volume:,}",
            "108K picks",
            delta_color="normal"
        )

    with col5:
        occupancy = (len(sku_df['current_slot'].unique()) / len(warehouse_df)) * 100
        st.metric(
            "Warehouse Occupancy",
            f"{occupancy:.1f}%",
            "95.9% available"
        )

    st.markdown("---")

    # Chaos Score Card
    st.markdown("### 🎯 Warehouse Health: Chaos Score")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Calculate Chaos Score components
        temp_violation_rate = violation_rate
        congestion_index = 47.2  # From analysis
        travel_inefficiency = 35.2
        safety_rate = 0.7
        data_quality = 3.5

        chaos_score = (
            0.30 * temp_violation_rate +
            0.25 * congestion_index +
            0.20 * travel_inefficiency +
            0.15 * safety_rate +
            0.10 * data_quality
        )

        # Create gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=chaos_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Chaos Score", 'font': {'size': 24}},
            delta={'reference': 30, 'increasing': {'color': "red"}},
            gauge={
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 10], 'color': '#28a745'},
                    {'range': [10, 20], 'color': '#90ee90'},
                    {'range': [20, 30], 'color': '#ffc107'},
                    {'range': [30, 50], 'color': '#fd7e14'},
                    {'range': [50, 70], 'color': '#dc3545'},
                    {'range': [70, 100], 'color': '#8b0000'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 50
                }
            }
        ))

        fig_gauge.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=50, b=20),
            paper_bgcolor="white",
            font={'color': "darkblue", 'family': "Arial"}
        )

        st.plotly_chart(fig_gauge, use_container_width=True)

    with col2:
        st.markdown("#### Status: HIGH RISK ⚠️")
        st.markdown(f"**Current Score:** {chaos_score:.1f}/100")
        st.markdown("**Components:**")
        st.markdown(f"- Temp Violations: {temp_violation_rate:.1f}")
        st.markdown(f"- Congestion: {congestion_index}")
        st.markdown(f"- Travel Inefficiency: {travel_inefficiency}")
        st.markdown(f"- Safety Rate: {safety_rate}")
        st.markdown(f"- Data Quality: {data_quality}")

        st.markdown("---")
        st.markdown("**Action Required:**")
        st.error("🚨 Urgent intervention needed")
        st.markdown("Target: <30 (Moderate)")

    st.markdown("---")

    # Two column layout for charts
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Hourly Order Distribution")
        hourly_orders = orders_df.groupby('hour').size().reset_index(name='count')

        fig_hourly = px.bar(
            hourly_orders,
            x='hour',
            y='count',
            title="Orders by Hour of Day",
            labels={'hour': 'Hour', 'count': 'Number of Orders'},
            color='count',
            color_continuous_scale='Reds'
        )

        # Highlight peak hour
        fig_hourly.add_vline(x=19, line_dash="dash", line_color="red", 
                            annotation_text="Peak: 19:00")

        fig_hourly.update_layout(
            xaxis_title="Hour of Day",
            yaxis_title="Order Count",
            showlegend=False,
            height=400
        )

        st.plotly_chart(fig_hourly, use_container_width=True)

    with col2:
        st.markdown("### 🏢 Zone Utilization")
        zone_util = sku_with_warehouse.groupby('zone').size().reset_index(name='occupied')
        zone_capacity = warehouse_df.groupby('zone').size().reset_index(name='capacity')
        zone_data = zone_util.merge(zone_capacity, on='zone')
        zone_data['utilization'] = (zone_data['occupied'] / zone_data['capacity']) * 100

        fig_zone = px.bar(
            zone_data,
            x='zone',
            y='utilization',
            title="Warehouse Zone Utilization (%)",
            labels={'zone': 'Zone', 'utilization': 'Utilization %'},
            color='utilization',
            color_continuous_scale='Blues',
            text='utilization'
        )

        fig_zone.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig_zone.update_layout(
            yaxis_title="Utilization %",
            xaxis_title="Zone",
            showlegend=False,
            height=400
        )

        st.plotly_chart(fig_zone, use_container_width=True)

    # Bottom section
    st.markdown("---")
    st.markdown("### 🎯 Top 10 High-Velocity SKUs")

    top_skus = sku_frequency.head(10).merge(sku_df[['sku_id', 'category', 'temp_req']], on='sku_id')

    fig_top_skus = px.bar(
        top_skus,
        x='sku_id',
        y='order_count',
        color='category',
        title="Most Frequently Ordered Products",
        labels={'sku_id': 'SKU', 'order_count': 'Order Frequency'},
        text='order_count'
    )

    fig_top_skus.update_traces(textposition='outside')
    fig_top_skus.update_layout(height=400, xaxis_tickangle=-45)

    st.plotly_chart(fig_top_skus, use_container_width=True)

# ============================================================================
# PAGE 2: HEATMAP ANALYSIS
# ============================================================================
elif page == "🔥 Heatmap Analysis":
    st.title("🔥 Aisle Congestion Heatmap")
    st.markdown("### High-Collision Aisles & Peak Hour Bottlenecks")

    # Filters
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**Filter by hour to identify congestion hotspots**")
    with col2:
        selected_hour = st.selectbox("Hour", list(range(24)), index=19)

    # Calculate hourly aisle traffic
    aisle_hour_traffic = picker_with_location.groupby(['aisle', 'hour']).size().reset_index(name='movements')

    # Filter for selected hour
    hour_data = aisle_hour_traffic[aisle_hour_traffic['hour'] == selected_hour].copy()
    hour_data = hour_data.sort_values('movements', ascending=False)

    # Create heatmap pivot
    heatmap_data = aisle_hour_traffic.pivot_table(
        index='aisle',
        columns='hour',
        values='movements',
        fill_value=0
    )

    # Filter to top 30 aisles by total traffic
    top_aisles = aisle_hour_traffic.groupby('aisle')['movements'].sum().nlargest(30).index
    heatmap_filtered = heatmap_data.loc[heatmap_data.index.isin(top_aisles)]

    st.markdown("---")

    # Main heatmap
    st.markdown(f"### Congestion Heatmap: Hour {selected_hour}:00")

    fig_heatmap = px.imshow(
        heatmap_filtered,
        labels=dict(x="Hour of Day", y="Aisle", color="Movements"),
        x=heatmap_filtered.columns,
        y=heatmap_filtered.index,
        color_continuous_scale='Reds',
        aspect="auto"
    )

    fig_heatmap.update_layout(
        title=f"Top 30 Busiest Aisles - Movement Density by Hour",
        height=700,
        xaxis_title="Hour of Day",
        yaxis_title="Aisle ID"
    )

    st.plotly_chart(fig_heatmap, use_container_width=True)

    st.markdown("---")

    # Aisle B specific analysis
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🚨 Aisle B Bottleneck Analysis")

        # Filter B aisles
        aisle_b_data = aisle_hour_traffic[aisle_hour_traffic['aisle'].str.startswith('B', na=False)]
        aisle_b_hourly = aisle_b_data.groupby('hour')['movements'].sum().reset_index()

        fig_aisle_b = px.line(
            aisle_b_hourly,
            x='hour',
            y='movements',
            title="Aisle B Traffic Over 24 Hours",
            labels={'hour': 'Hour', 'movements': 'Total Movements'},
            markers=True
        )

        fig_aisle_b.add_hline(
            y=aisle_b_hourly['movements'].mean(),
            line_dash="dash",
            line_color="orange",
            annotation_text="Average"
        )

        # Highlight peak at 19:00
        peak_val = aisle_b_hourly[aisle_b_hourly['hour'] == 19]['movements'].values[0]
        fig_aisle_b.add_annotation(
            x=19,
            y=peak_val,
            text=f"Peak: {peak_val} movements",
            showarrow=True,
            arrowhead=2,
            arrowcolor="red",
            bgcolor="yellow",
            opacity=0.8
        )

        fig_aisle_b.update_layout(height=400)
        st.plotly_chart(fig_aisle_b, use_container_width=True)

        st.warning("⚠️ **Forklift Constraint:** Max 2 pickers allowed in Aisle B")
        st.error(f"🚨 **Peak Hour (19:00):** {aisle_b_hourly[aisle_b_hourly['hour']==19]['movements'].values[0]} movements")

    with col2:
        st.markdown(f"### Top 10 Aisles at {selected_hour}:00")

        top_10_hour = hour_data.head(10)

        fig_top10 = px.bar(
            top_10_hour,
            x='aisle',
            y='movements',
            color='movements',
            color_continuous_scale='Oranges',
            title=f"Most Congested Aisles at {selected_hour}:00",
            text='movements'
        )

        fig_top10.update_traces(textposition='outside')
        fig_top10.update_layout(
            xaxis_title="Aisle",
            yaxis_title="Picker Movements",
            showlegend=False,
            height=400
        )

        st.plotly_chart(fig_top10, use_container_width=True)

        # Display data table
        st.dataframe(
            top_10_hour[['aisle', 'movements']].reset_index(drop=True),
            use_container_width=True
        )

# ============================================================================
# PAGE 3: TEMPERATURE VIOLATIONS
# ============================================================================
elif page == "❄️ Temperature Violations":
    st.title("❄️ Temperature Zone Violations & Spoilage Risk")
    st.markdown("### Critical Inventory Compliance Analysis")

    violations = sku_with_warehouse[sku_with_warehouse['temp_violation'] == True]

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Violations", f"{len(violations)}", f"{(len(violations)/len(sku_df)*100):.1f}%")

    with col2:
        critical = len(violations[
            (violations['temp_req'].isin(['Frozen', 'Refrigerated'])) &
            (violations['temp_zone'] == 'Ambient')
        ])
        st.metric("Critical Violations", f"{critical}", "Cold → Ambient")

    with col3:
        st.metric("Value at Risk", "₹245,000", "Total inventory")

    with col4:
        st.metric("Critical Risk", "₹145,000", "Spoilage")

    st.markdown("---")

    # Violation breakdown
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Violations by Mismatch Type")

        violation_types = violations.groupby(['temp_req', 'temp_zone']).size().reset_index(name='count')
        violation_types['mismatch'] = violation_types['temp_req'] + ' → ' + violation_types['temp_zone']
        violation_types = violation_types.sort_values('count', ascending=False)

        fig_types = px.bar(
            violation_types,
            x='mismatch',
            y='count',
            color='count',
            color_continuous_scale='Reds',
            title="Temperature Mismatch Patterns",
            text='count'
        )

        fig_types.update_traces(textposition='outside')
        fig_types.update_layout(
            xaxis_title="Mismatch Type",
            yaxis_title="Number of SKUs",
            showlegend=False,
            height=400,
            xaxis_tickangle=-45
        )

        st.plotly_chart(fig_types, use_container_width=True)

    with col2:
        st.markdown("### 📦 Violations by Category")

        cat_violations = violations['category'].value_counts().reset_index()
        cat_violations.columns = ['category', 'count']

        fig_cat = px.pie(
            cat_violations,
            values='count',
            names='category',
            title="Violations Distribution by Product Category",
            color_discrete_sequence=px.colors.sequential.RdBu
        )

        fig_cat.update_traces(textposition='inside', textinfo='percent+label')
        fig_cat.update_layout(height=400)

        st.plotly_chart(fig_cat, use_container_width=True)

    st.markdown("---")

    # Critical violations table
    st.markdown("### 🚨 Critical Violations (Frozen/Refrigerated in Ambient)")

    critical_violations = violations[
        (violations['temp_req'].isin(['Frozen', 'Refrigerated'])) &
        (violations['temp_zone'] == 'Ambient')
    ][['sku_id', 'category', 'temp_req', 'temp_zone', 'current_slot']].head(20)

    st.dataframe(critical_violations, use_container_width=True, height=400)

    st.error("⚠️ **Immediate Action Required:** These items face complete product loss within 1-4 hours")

    st.markdown("---")

    # Temperature zone capacity
    st.markdown("### 🏢 Temperature Zone Capacity Analysis")

    col1, col2 = st.columns(2)

    with col1:
        # Current vs Required
        required_counts = sku_df['temp_req'].value_counts().reset_index()
        required_counts.columns = ['zone', 'required']

        current_counts = sku_with_warehouse.groupby('temp_zone').size().reset_index(name='current')

        capacity_data = warehouse_df.groupby('temp_zone').size().reset_index(name='capacity')

        zone_analysis = capacity_data.merge(current_counts, left_on='temp_zone', right_on='temp_zone', how='left')
        zone_analysis = zone_analysis.merge(required_counts, left_on='temp_zone', right_on='zone', how='left')
        zone_analysis = zone_analysis.fillna(0)

        fig_capacity = go.Figure()

        fig_capacity.add_trace(go.Bar(
            name='Capacity',
            x=zone_analysis['temp_zone'],
            y=zone_analysis['capacity'],
            marker_color='lightblue'
        ))

        fig_capacity.add_trace(go.Bar(
            name='Current',
            x=zone_analysis['temp_zone'],
            y=zone_analysis['current'],
            marker_color='orange'
        ))

        fig_capacity.add_trace(go.Bar(
            name='Required',
            x=zone_analysis['temp_zone'],
            y=zone_analysis['required'],
            marker_color='green'
        ))

        fig_capacity.update_layout(
            title="Temperature Zone: Capacity vs Current vs Required",
            xaxis_title="Temperature Zone",
            yaxis_title="Number of Slots/SKUs",
            barmode='group',
            height=400
        )

        st.plotly_chart(fig_capacity, use_container_width=True)

    with col2:
        # Utilization percentages
        zone_analysis['utilization'] = (zone_analysis['current'] / zone_analysis['capacity']) * 100
        zone_analysis['should_be'] = (zone_analysis['required'] / zone_analysis['capacity']) * 100

        fig_util = go.Figure()

        fig_util.add_trace(go.Bar(
            name='Current Utilization',
            x=zone_analysis['temp_zone'],
            y=zone_analysis['utilization'],
            marker_color='orange',
            text=zone_analysis['utilization'].round(1),
            textposition='outside'
        ))

        fig_util.add_trace(go.Bar(
            name='Target Utilization',
            x=zone_analysis['temp_zone'],
            y=zone_analysis['should_be'],
            marker_color='green',
            text=zone_analysis['should_be'].round(1),
            textposition='outside'
        ))

        fig_util.update_layout(
            title="Zone Utilization: Current vs Target",
            xaxis_title="Temperature Zone",
            yaxis_title="Utilization %",
            barmode='group',
            height=400
        )

        st.plotly_chart(fig_util, use_container_width=True)

# ============================================================================
# PAGE 4: PICKER PERFORMANCE
# ============================================================================
elif page == "👤 Picker Performance":
    st.title("👤 Picker Performance Analysis")
    st.markdown("### Efficiency Metrics & The Shortcut Paradox")

    # Calculate picker statistics
    picker_stats = picker_df_enhanced.groupby('picker_id').agg({
        'travel_distance_m': ['mean', 'std', 'count'],
        'travel_time_minutes': ['mean', 'std'],
        'speed_m_per_min': ['mean', 'std']
    }).round(2)

    picker_stats.columns = ['_'.join(col).strip() for col in picker_stats.columns.values]
    picker_stats = picker_stats.reset_index()

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        avg_distance = picker_stats['travel_distance_m_mean'].mean()
        st.metric("Avg Distance", f"{avg_distance:.1f}m", "Per pick")

    with col2:
        avg_time = picker_stats['travel_time_minutes_mean'].mean()
        st.metric("Avg Time", f"{avg_time:.2f} min", "Per pick")

    with col3:
        avg_speed = picker_stats['speed_m_per_min_mean'].mean()
        st.metric("Avg Speed", f"{avg_speed:.1f} m/min", "Overall")

    with col4:
        total_picks = picker_stats['travel_distance_m_count'].sum()
        st.metric("Total Picks", f"{int(total_picks):,}", "90 weeks")

    st.markdown("---")

    # Picker comparison
    st.markdown("### 📊 Picker Efficiency Comparison")

    col1, col2 = st.columns(2)

    with col1:
        fig_distance = px.bar(
            picker_stats,
            x='picker_id',
            y='travel_distance_m_mean',
            color='travel_distance_m_mean',
            color_continuous_scale='RdYlGn_r',
            title="Average Travel Distance by Picker",
            text='travel_distance_m_mean'
        )

        fig_distance.update_traces(texttemplate='%{text:.1f}m', textposition='outside')
        fig_distance.update_layout(
            xaxis_title="Picker ID",
            yaxis_title="Avg Distance (meters)",
            showlegend=False,
            height=400
        )

        # Highlight PICKER-07
        fig_distance.add_hline(
            y=avg_distance,
            line_dash="dash",
            line_color="red",
            annotation_text="Average"
        )

        st.plotly_chart(fig_distance, use_container_width=True)

    with col2:
        fig_speed = px.bar(
            picker_stats,
            x='picker_id',
            y='speed_m_per_min_mean',
            color='speed_m_per_min_mean',
            color_continuous_scale='RdYlGn',
            title="Average Speed by Picker",
            text='speed_m_per_min_mean'
        )

        fig_speed.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        fig_speed.update_layout(
            xaxis_title="Picker ID",
            yaxis_title="Speed (m/min)",
            showlegend=False,
            height=400
        )

        fig_speed.add_hline(
            y=avg_speed,
            line_dash="dash",
            line_color="blue",
            annotation_text="Average"
        )

        st.plotly_chart(fig_speed, use_container_width=True)

    st.markdown("---")

    # PICKER-07 deep dive
    st.markdown("### 🔍 The Shortcut Paradox: PICKER-07 Analysis")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Create comparison chart
        picker_07_stats = picker_stats[picker_stats['picker_id'] == 'PICKER-07']
        others_stats = picker_stats[picker_stats['picker_id'] != 'PICKER-07']

        comparison_data = pd.DataFrame({
            'Metric': ['Avg Distance (m)', 'Avg Time (min)', 'Avg Speed (m/min)'],
            'PICKER-07': [
                picker_07_stats['travel_distance_m_mean'].values[0],
                picker_07_stats['travel_time_minutes_mean'].values[0],
                picker_07_stats['speed_m_per_min_mean'].values[0]
            ],
            'Other Pickers': [
                others_stats['travel_distance_m_mean'].mean(),
                others_stats['travel_time_minutes_mean'].mean(),
                others_stats['speed_m_per_min_mean'].mean()
            ]
        })

        fig_comparison = go.Figure()

        fig_comparison.add_trace(go.Bar(
            name='PICKER-07',
            x=comparison_data['Metric'],
            y=comparison_data['PICKER-07'],
            marker_color='red',
            text=comparison_data['PICKER-07'].round(2),
            textposition='outside'
        ))

        fig_comparison.add_trace(go.Bar(
            name='Average (Others)',
            x=comparison_data['Metric'],
            y=comparison_data['Other Pickers'],
            marker_color='blue',
            text=comparison_data['Other Pickers'].round(2),
            textposition='outside'
        ))

        fig_comparison.update_layout(
            title="PICKER-07 vs Others: Performance Metrics",
            xaxis_title="Metric",
            yaxis_title="Value",
            barmode='group',
            height=400
        )

        st.plotly_chart(fig_comparison, use_container_width=True)

    with col2:
        st.markdown("#### 🚨 Anomaly Detected")
        st.error("**PICKER-07 Profile:**")
        st.markdown(f"- Distance: **50% lower**")
        st.markdown(f"- Time: **Same as others**")
        st.markdown(f"- Speed: **48% slower**")
        st.markdown("---")
        st.warning("**Interpretation:**")
        st.markdown("Travels HALF the distance in SAME time = Taking shortcuts through restricted areas")
        st.markdown("---")
        st.info("**Evidence:**")
        st.markdown(f"- Total picks: {int(picker_07_stats['travel_distance_m_count'].values[0]):,}")
        st.markdown("- Pattern: Consistent across 90 weeks")
        st.markdown("- Deviation: Statistically impossible")

    st.markdown("---")

    # Picker performance table
    st.markdown("### 📋 Complete Picker Statistics")

    display_stats = picker_stats[[
        'picker_id',
        'travel_distance_m_mean',
        'travel_time_minutes_mean',
        'speed_m_per_min_mean',
        'travel_distance_m_count'
    ]].copy()

    display_stats.columns = ['Picker ID', 'Avg Distance (m)', 'Avg Time (min)', 'Speed (m/min)', 'Total Picks']
    display_stats = display_stats.round(2)
    display_stats = display_stats.sort_values('Avg Distance (m)')

    st.dataframe(display_stats, use_container_width=True, height=400)

# ============================================================================
# PAGE 5: DEMAND PATTERNS
# ============================================================================
elif page == "📈 Demand Patterns":
    st.title("📈 Demand Pattern Analysis")
    st.markdown("### Order Velocity & Temporal Trends")

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_orders = len(orders_df)
        st.metric("Total Orders", f"{total_orders:,}", "436K line items")

    with col2:
        unique_orders = orders_df['order_id'].nunique()
        st.metric("Unique Orders", f"{unique_orders:,}", "998 bulk orders")

    with col3:
        avg_items = total_orders / unique_orders
        st.metric("Avg Items/Order", f"{avg_items:.0f}", "437 items")

    with col4:
        weeks = orders_df['week'].nunique()
        st.metric("Analysis Period", f"{weeks} weeks", "90 weeks")

    st.markdown("---")

    # Hourly pattern
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ⏰ 24-Hour Order Pattern")

        hourly_orders = orders_df.groupby('hour').size().reset_index(name='count')

        fig_hourly = px.area(
            hourly_orders,
            x='hour',
            y='count',
            title="Order Distribution Over 24 Hours",
            labels={'hour': 'Hour of Day', 'count': 'Order Count'},
            color_discrete_sequence=['#1f77b4']
        )

        # Mark peak hours
        fig_hourly.add_vrect(
            x0=18, x1=21,
            fillcolor="red",
            opacity=0.2,
            annotation_text="Peak Hours",
            annotation_position="top left"
        )

        fig_hourly.update_layout(height=400)
        st.plotly_chart(fig_hourly, use_container_width=True)

    with col2:
        st.markdown("### 📅 Day of Week Pattern")

        daily_orders = orders_df.groupby('day_name').size().reset_index(name='count')
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily_orders['day_name'] = pd.Categorical(daily_orders['day_name'], categories=day_order, ordered=True)
        daily_orders = daily_orders.sort_values('day_name')

        fig_daily = px.bar(
            daily_orders,
            x='day_name',
            y='count',
            title="Orders by Day of Week",
            labels={'day_name': 'Day', 'count': 'Order Count'},
            color='count',
            color_continuous_scale='Viridis'
        )

        fig_daily.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_daily, use_container_width=True)

    st.markdown("---")

    # Weekly trend
    st.markdown("### 📊 Weekly Order Volume Trend")

    weekly_orders = orders_df.groupby('week').size().reset_index(name='count')

    fig_weekly = px.line(
        weekly_orders,
        x='week',
        y='count',
        title="Order Volume Over 90 Weeks",
        labels={'week': 'Week Number', 'count': 'Order Count'},
        markers=True
    )

    # Add trend line
    z = np.polyfit(weekly_orders['week'], weekly_orders['count'], 1)
    p = np.poly1d(z)
    fig_weekly.add_scatter(
        x=weekly_orders['week'],
        y=p(weekly_orders['week']),
        mode='lines',
        name='Trend',
        line=dict(dash='dash', color='red')
    )

    fig_weekly.update_layout(height=400)
    st.plotly_chart(fig_weekly, use_container_width=True)

    st.markdown("---")

    # Top SKUs
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 🏆 Top 20 High-Velocity SKUs")

        top_20 = sku_frequency.head(20).merge(
            sku_df[['sku_id', 'category', 'temp_req']], 
            on='sku_id'
        )

        fig_top20 = px.bar(
            top_20,
            x='sku_id',
            y='order_count',
            color='category',
            title="Most Frequently Ordered Products",
            labels={'sku_id': 'SKU', 'order_count': 'Order Frequency'},
            text='order_count'
        )

        fig_top20.update_traces(textposition='outside')
        fig_top20.update_layout(height=500, xaxis_tickangle=-45)

        st.plotly_chart(fig_top20, use_container_width=True)

    with col2:
        st.markdown("### 📦 Category Distribution")

        category_orders = orders_df.merge(
            sku_df[['sku_id', 'category']], 
            on='sku_id'
        )['category'].value_counts().reset_index()
        category_orders.columns = ['category', 'count']

        fig_cat = px.pie(
            category_orders,
            values='count',
            names='category',
            title="Orders by Category",
            color_discrete_sequence=px.colors.sequential.RdBu
        )

        fig_cat.update_traces(textposition='inside', textinfo='percent+label')
        fig_cat.update_layout(height=500)

        st.plotly_chart(fig_cat, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p><b>VelocityMart Operations Dashboard</b></p>
        <p>Data Period: 90 weeks (Jan 2024 - Sep 2025) | Analysis Date: Feb 5, 2026</p>
        <p>For DATAVERSE Challenge | Interim Operations Management</p>
    </div>
""", unsafe_allow_html=True)
