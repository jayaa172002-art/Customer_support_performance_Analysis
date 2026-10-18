# Customer_support_performance_Analysis
I worked on this project because i wanted to understand how a support team really works- what kind of tickets come in, which ones takes longest and what actually affects customer satisfaction (CSAT).

# Business Problem
The support team was getting a lot of tickets and some were breaching SLA (16.48% breach). I wanted to find out why tickets get delayed and what we can fix.

# About Data
- 8500+ support tickets
- Columns: Ticket ID, Created Date, Category, Priority, Channel, Status, Resolution Time, CSAT
- Raw data was messy - had blank CSAT scores and date format issues

# What I did to clean it:
- Used Python to clean the data - handled missing CSAT values, fixed dates
- Created a proper measure in power BI AVG CSAT Fixed to ignore blanks while calculating average

# Files in this Repo
- Customer_Support_Analyzer/data/ - raw and cleaned CSV files
- Customer_support_Analyzer/scripts/cleaning.py - my python cleaning code
- Customer_Support_CSAT_Performance_Dashboard.pbix - Final Power BI dashboard

# Dashboard - what I built
I built 3 visuals on the main performance page:
1. CSAT Trend Over Time (Monthly): Shows CSAT from Jan to Dec. It is not stable - went highest 3.17 in March and lowest 2.85 in Nov. So customer experience is inconsistent across months.
2. Volume vs Resolution Time Matrix: This one gave the best insight. Refund Request and Cancellation Request have both high volume and high resolution time (8+ hours avg). So they are the biggest bottleneck.
3. Ticket Volume by Support Channel: To see where most workload comes from - Email, Phone, Chat, Social etc.

# Key Findings
- Refund Request (1756 tickets) + Cancellation Request (1695 tickets) = 3451 tickets, which is almost 40% of all tickets.
-  These same 2 categories take longest to resolve - 8.1 and 8.2 hours on average.
-  If we fix just these two, we can reduce a lot of agent workload.

# MY Recommendation
Automate or create self-help for Refund and Cancellation requests. If customers can self-serve these, we can save 3000+ hours of agent time, reduce SLA breach from 16.48% and improve CSAT.

# Tools I used
Power BI, DAX, Python(Pandas), Data Cleaning, Data Visualization

