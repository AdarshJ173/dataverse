
Skip to main content

    Company
    Newsroom
    Careers
    USA - EN
    Locations
    Your Workspace

Back to home - Geodis, customized logistics solutions

    Find Your Solution
    Why GEODIS
    Blog & Resources
            three trucks with human aid on it
            employee preparing a package for delivery
    Contact Us

Your search:
You are here :

    Home
    Blog
    Warehouse Optimization: Slotting & Wave Pick Improvement

A woman using a Locus Robotics device to pick items at a warehouse

04/17/2025
Warehouse Optimization: Slotting & Wave Pick Improvement
Unlock the technical foundations of warehouse efficiency with our data-driven approach to inventory placement and order processing that delivers 15-60% performance improvements.

While most warehouse managers understand that efficiency is critical, the technical aspects of how to achieve substantial improvements often remain mysterious. At GEODIS, we've developed sophisticated methodologies for our warehouse optimization that go beyond conventional approaches. Our integrated solution combines strategic inventory placement with intelligent order processing—turning data into actionable improvements that reduce picker travel time by up to 70%.

 

In this article, we dive deep into the technical foundation of our warehouse optimization approach, explaining exactly how our slotting and wave pick techniques work together to transform the warehousing operations that we run on your behalf. 

 

Download our Warehouse Optimization white paper here.
Key takeaways

 

    Effective slotting optimization places items strategically based on 52 weeks of movement data, with customized machine learning models for each SKU
    Wave picking techniques use advanced algorithms to minimize aisle visits, reducing travel by up to 47% per task
    Data-driven decision making enables continuous optimization through individual SKU forecasting models and location ranking
    The integration of slotting and wave optimization creates complementary effects that maximize warehouse efficiency
    Our technical approach adapts to different picking methodologies and warehouse configurations, including automated environments
    Implementation requires minimal disruption to operations while delivering 15-60% efficiency improvements

Slotting optimization: Technical foundation and methodology

Slotting optimization addresses a fundamental warehouse challenge: placing the right item in the right location at the right time. While the concept seems simple, effective implementation requires sophisticated data analysis and methodical execution.

 
Smart location assignment

Our slotting optimization system employs a data-driven approach to inventory placement:

 

    Data analysis: The system analyzes 52 weeks of rolling historical order data, refreshed weekly, to identify item movement patterns
     
    Item ranking: Products are ranked based on velocity, volume, and other metrics tailored to each client's operational priorities
     
    Location ranking: Warehouse locations are ranked using picking zones and picking sequences, with high-rank items placed near outbound areas to minimize travel time
     
    Location assignment: The system matches items to locations based on their respective rankings, following the shortest distance algorithm

 

This approach ensures that your most frequently picked items are placed in the most accessible locations, dramatically reducing overall travel time.

 
SKU velocity analysis and segmentation

Not all products move at the same rate. Our system uses advanced analytics to understand these differences and optimize accordingly:

 

    Individual forecasting models: We develop dedicated machine learning models for each SKU using the open-source Facebook Prophet time series framework, which effectively handles seasonal patterns and trend changes
    Adaptive tuning: Models are tuned based on demand variability segmentation, allowing for customized forecasting approaches based on each SKU's unique characteristics
    Rolling analysis: The system analyzes 52 weeks of rolling historical data, refreshed weekly, ensuring that optimization decisions reflect the most current demand patterns
    Segmentation framework: SKUs are classified using an ADI-CV² framework (Average Demand Interval and Coefficient of Variation), an industry-standard approach that segments products based on their demand patterns

 

This granular approach to inventory analysis ensures that warehouse layouts reflect actual usage patterns rather than assumptions or conventions.

 
Dead and slow stock management

One of the most powerful aspects of slotting optimization is identifying and relocating inventory that occupies valuable warehouse space without delivering value:

 

    Dead stock identification: Items with no orders in the past 6+ months are flagged as dead stock for potential relocation
    Slow mover designation: Products that have been in a warehouse for more than three months with a weekly average pick of 10 units or fewer are classified as slow movers
    Strategic relocation: Dead and slow-moving stock is moved from prime picking locations to designated areas, freeing up valuable real estate for high-velocity products

 

Our pilot implementations have shown that stock management alone can significantly improve efficiency. In one implementation, relocating dead and slow movers from prime pick fronts contributed to a 30% increase in units picked per hour.
warehousing_slotting_optimization_process_flow.jpg

Contact our experts to discover how GEODIS can optimize your inventory placement in our warehouses for maximum efficiency. Get in touch with GEODIS.
Contact us
Wave pick optimization: Technical approaches and implementation

While slotting optimization focuses on where items are placed, wave pick optimization addresses how orders are grouped and picked. Our technical approach to wave picking minimizes travel distance through sophisticated algorithms and data-driven methodologies.

 
Intelligent order batching

Our wave pick optimization system groups orders together in a way that minimizes the total distance traveled by pickers:

 

    Order analysis: The system analyzes incoming orders and their line items
     
    Pick type determination: Orders are assigned pick types (batch, order, line) based on item characteristics and warehouse zones
     
    Grouping and sequencing: Orders are grouped based on parameters like carrier, delivery service, and ship date, then sequenced by priority
     
    Batch optimization: Algorithms create optimal batches considering cart capacity, picker availability, and aisle minimization

 

This approach significantly reduces redundant travel. Our pilot implementation showed that aisle visits per task decreased by 47% on average, with some facilities experiencing reductions of more than 80% in specific scenarios.

 
Wave optimization process flow

Our wave optimization follows a structured, data-driven process that transforms individual orders into optimized picking groups:

 

    Order data collection: The system gathers all available orders within the specified timeframe, typically aligned with warehouse cut-off times and shipping schedules
     
    Pick type classification: Each order is assigned a specific pick type (batch, batch singles, order, or line) based on its items' characteristics and the zones where they're located
     
    Parameter-based grouping: Orders are grouped based on multiple operational parameters that can include:
     
        Carrier service requirements
        Delivery time commitments
        Requested ship dates
        Order priority levels
        Shipping terminals
        Special handling requirements (e.g., hazardous materials)
         
    Sequencing by priority: These groups are sequenced based on operational priorities such as cut-off times, service level agreements, and order urgency
     
    Optimal batch formation: The system applies our aisle minimization algorithm to create batches that minimize travel distance while respecting constraints like cart capacity and picker availability
     
    Wave release and execution: Once optimized, waves are released to the warehouse floor as pick tasks, which pickers or automated systems can execute efficiently

 

This structured approach ensures that every wave maximizes picker productivity by minimizing unnecessary travel while still meeting all service level requirements. The process can be repeated multiple times throughout the day, adapting to changing order patterns and operational conditions in real-time.

 
Aisle minimization algorithm

At the heart of wave optimization is our aisle minimization algorithm:

 

    Clustering analysis: The system identifies orders that can be picked together with minimal aisle visits
    Order correlation: Orders with complementary pick locations are grouped together
    Path optimization: Pick paths are designed to minimize aisle traversal while simplifying operations
    S-shape routing optimization: Our algorithms are optimized for S-shape picking patterns, which are intuitive for pickers while still delivering substantial efficiency improvements

 

In our client implementations, this algorithm has reduced aisle visits by between 15% and 60%. Well-organized facilities saw 15-20% improvements with less optimized operations experiencing even more dramatic gains.

 
Congestion management for modern picking

Wave optimization extends beyond traditional picking to address unique challenges in automated environments:

 

    Locus robot optimization: For facilities using Locus robots (automated warehouse picking robots), the system distributes high-velocity items across aisles to prevent congestion
    Wave template diversification: Multiple wave templates create varied paths for pickers or robots, reducing bottlenecks in high-traffic areas
    Strategic high-mover placement: High movers are distributed across multiple aisles rather than concentrated in a single area

 

One client using this approach for a new product launch saw a 50% reduction in congestion compared to the previous year's launch. This significantly improved picking rates, even when using automated systems.
wave_pick_warehouse_optimization_process.jpg

Ready to optimize your picking operations? Contact our logistics experts to learn how our warehouses reduce travel time and increase productivity. Get in touch with GEODIS.
Contact us
Data-driven decision making

The effectiveness of our warehouse optimization solution relies on sophisticated data analysis and machine learning capabilities.

 
Comprehensive data analysis

Our system uses extensive historical data to drive optimization decisions:

 

    52-week rolling data analysis: The system examines a full year of order data, creating a comprehensive picture of demand patterns, seasonal trends, and item relationships
    Weekly data refresh: Data is updated weekly, ensuring that optimization decisions reflect the most current patterns
    SKU-level granularity: Analysis is performed at the individual SKU level, capturing the unique characteristics of each product
    Location-level mapping: Warehouse locations are analyzed based on access time, proximity to outbound areas, and picking efficiency

 
Machine learning models

Advanced analytics power our optimization decisions:

 

    Individual SKU forecasting: We create dedicated machine learning models for each SKU to predict future demand patterns
    Facebook Prophet framework: Our forecasting uses the open-source Facebook Prophet time series model, which handles seasonal patterns, trend changes, and irregular events
    Adaptive model tuning: Models are tuned based on demand characteristics, with different parameters for stable, seasonal, and volatile items

 
Performance measurement and visualization

Continuous performance tracking ensures sustained improvements:

 

    Comprehensive dashboards: PowerBI dashboards provide deep insight into SKU-level data, weekly predictions, and optimization results
    Key metric tracking: The system monitors metrics like aisle visits, units per hour, and travel distance
    Performance visualization: Graphical representations help identify opportunities for further optimization
    Continuous refinement: Algorithms are regularly refined based on actual performance data

PICT068660-Feltham-HALLEN Nilkas
Integration of slotting and wave optimization

The true power of our solution comes from the integration of slotting and wave optimization. These components work together to create complementary effects that maximize warehouse efficiency.

 
Complementary approaches

Slotting and wave optimization address different aspects of warehouse efficiency, but they work together to create a unified solution:

 

    Slotting optimizes location: Strategic inventory placement ensures that high-velocity items are in accessible locations
    Wave optimization optimizes tasks: Intelligent order batching minimizes travel for each picking task
    Combined impact: When implemented together, these approaches create synergistic effects that maximize overall efficiency

 

While each component delivers benefits independently, the integrated approach provides the greatest improvements. Good slotting without good waving still results in suboptimal picking groups, while good waving without good slotting means items aren't optimally placed.

 
Technical implementation

Implementing both components requires careful coordination:

 

    Complementary data models: Slotting and wave optimization share underlying data models, ensuring consistent decision-making
    Sequential implementation: Components can be implemented in either order, with each enhancing the effectiveness of the other
    Continuous coordination: Ongoing coordination between components ensures optimal performance

 
Adaptive optimization

Our integrated solution adapts to changing conditions:

 

    Continuous reassessment: The system continually reassesses inventory placement and order batching
    Seasonal adaptability: Optimization adjusts to seasonal demand patterns
    New product accommodation: The system adapts to new product introductions and discontinuation

 

This adaptive approach ensures that warehouse operations remain optimized even as conditions change.
integrated_warehouse_optimization_framework.jpg
Technology foundation

Our warehouse optimization combines advanced analytics with deep operational knowledge to deliver practical, impactful improvements.

 
System architecture

The warehouse optimization solution is built on a flexible architecture:

 

    Modular components: Slotting and wave optimization can be implemented independently or together, allowing for phased implementation
    API-based integration: Local API with HTML user interface enables interaction with existing warehouse management systems
    Dashboard visualization: PowerBI dashboard provides comprehensive visibility into SKU data, slotting recommendations, and performance metrics
    Parameter configuration: The system allows for customization of key parameters including batch sizes, volume thresholds, and picking methodologies

 
Technical methodologies

Sophisticated methodologies drive our optimization decisions:

 

    Location ranking methodology: Our location optimization uses a multi-factor ranking approach that considers picking zone prioritization, sequence-based distance calculation, ergonomic considerations, and specialized location types
    Wave optimization algorithms: Our wave optimization uses advanced clustering and path minimization techniques, including aisle minimization algorithms, star aisle methodology, pick sequence distance approximation, and S-shape routing optimization
    SKU forecasting methodology: Our slotting optimization relies on accurate SKU-level demand forecasting with individual SKU models, adaptive tuning, rolling analysis, and segmentation frameworks

 
Adaptability to diverse environments

Our solution is designed to accommodate the unique characteristics of various facilities:

 

    Layout flexibility: Whether your warehouse uses traditional racking, automated storage and retrieval systems, or a combination of storage types, our solution adapts to your specific layout
    Diverse picking methodologies: The solution supports multiple picking strategies including S-shape, return method, mid-point, and largest gap approaches
    Varying facility sizes: Our approach scales effectively from smaller distribution centers to massive fulfillment operations

 

This adaptability means we can implement our warehouse optimization solution across our network of facilities, achieving significant efficiency gains without disrupting established operations.

 
Explore our warehouse optimization series

Want to learn more about our warehouse optimization approach? Explore these in-depth articles:

 

    Maximize Warehouse Efficiency: The GEODIS Approach to Optimization - Get a high-level overview of our integrated warehouse optimization solution
    Modern Warehouse Challenges and Optimization - Dive deep into the challenges facing modern warehouses and how integrated optimization addresses them
    Real-World Warehouse Optimization: Results & Impact - Discover real-world case studies and learn about our implementation process

How GEODIS can help

GEODIS offers a streamlined implementation process to optimize your operations in our warehouses:

 

    Quick implementation: Each component (slotting and wave optimization) takes just 2-3 weeks to implement
    Minimal disruption: The system works alongside our existing operations with no need for physical reconfiguration
    Continuous refinement: Ongoing analysis and adjustment maintain optimal performance
    Comprehensive support: Our team guides you through each step of the process

 

Our approach is tailored to your specific needs:

 

    Customizable business rules: We define specific rules for wave planning, including criteria for grouping orders by carrier, delivery service, requested ship date, or other business-critical factors
    Adjustable batch sizes: Batch size parameters are tailored to match picking cart capacity, picker capabilities, and order characteristics for your operation
    Flexible volume thresholds: For facilities requiring cartonization, volume thresholds are adjusted to align with specific packaging requirements
    Pick zone prioritization: We define custom rules for prioritizing picking zones based on your warehouse layout and operational priorities

 

The result? Reduced labor costs, increased throughput, improved service level compliance, and better space utilization—all without the need for significant physical changes to your operations.

 

Get in touch with GEODIS. 
Contact us
FAQs about warehouse slotting and waving improvements
Paul Maplesden
Paul Maplesden
Lead Content Strategist
Paul deeply researches logistics and supply chain topics to create helpful, informative content for our US audience. Read Paul's work in the GEODIS blog, our in-depth GEODIS Insights reports, and our case studies and white papers.
Follow Paul on LinkedIn
Table of content

    Key takeaways
    Slotting optimization: Technical foundation and methodology
    Wave pick optimization: Technical approaches and implementation
    Data-driven decision making
    Integration of slotting and wave optimization
    Technology foundation
    Explore our warehouse optimization series
    How GEODIS can help
    FAQs about warehouse slotting and waving improvements

logo-geodis

    About us
    History
    Governance
    Purpose & Core Values
    Lines of Business
    Social Responsibility
    Newsroom
    Careers

    Transport Services
    Freight Solutions
    Warehousing & Value Added Logistics
    Industry Solutions

    Get a quote
    Contact an Expert
    Track your parcel
    Emissions Calculator
    Accessibility
    Customer Advisory
    Standard Trading Conditions and Certifications
    Sitemap

FOLLOW US

    logo-instagram
    logo-twitter
    logo-youtube
    linkedin-logo

CHANGE LANGUAGE
USA - EN
©2026 GEODIS all rights reserved
Manage cookies
Privacy policy
Legal information
Terms of use
Vulnerability disclosure
logo sncf
