\### 🧠 Full Causal DAG



```mermaid

graph TD

&nbsp; %% Unobserved confounders (hidden variables)

&nbsp; CQ\[Customer Quality Score<br/><i>unobserved</i>]

&nbsp; CC\[Carrier Capability Score<br/><i>unobserved</i>]



&nbsp; %% Observable confounders

&nbsp; CS\[Customer Segment<br/><i>Enterprise/Repeat/New</i>]

&nbsp; T\[Time<br/><i>Days since start</i>]

&nbsp; SL\[Service Level<br/><i>Standard/Express/Overnight</i>]



&nbsp; %% Treatment variables

&nbsp; PR\[Post Rollout<br/><i>Date ≥ April 1</i>]

&nbsp; AS\[Algorithmic Selection<br/><i>Treatment</i>]



&nbsp; %% Intermediate variables

&nbsp; CarrierSel\[Carrier Selection<br/><i>Which carrier chosen</i>]



&nbsp; %% Outcome variables

&nbsp; DT\[Delivery Time]

&nbsp; Cost\[Shipment Cost]

&nbsp; OT\[On-Time Delivery]

&nbsp; Sat\[Customer Satisfaction]



&nbsp; %% Survey response mechanism

&nbsp; SR\[Survey Response<br/><i>Missing data mechanism</i>]



&nbsp; %% Confounding paths (create bias)

&nbsp; CQ --> CS

&nbsp; CQ --> AS

&nbsp; CQ --> DT

&nbsp; CQ --> Cost

&nbsp; CQ --> Sat



&nbsp; CC --> CarrierSel

&nbsp; CC --> DT

&nbsp; CC --> Cost

&nbsp; CC --> OT



&nbsp; CS --> AS

&nbsp; T --> AS

&nbsp; T --> DT

&nbsp; T --> Cost



&nbsp; PR --> AS

&nbsp; CS --> AS



&nbsp; AS --> CarrierSel

&nbsp; CQ --> CarrierSel



&nbsp; SL --> DT

&nbsp; SL --> Cost

&nbsp; CarrierSel --> SL



&nbsp; AS --> DT

&nbsp; AS --> Cost

&nbsp; AS --> OT

&nbsp; AS --> Sat



&nbsp; CarrierSel --> DT

&nbsp; CarrierSel --> Cost

&nbsp; CarrierSel --> OT



&nbsp; OT --> Sat

&nbsp; DT --> OT



&nbsp; OT --> SR

&nbsp; CS --> SR

&nbsp; SR --> Sat



&nbsp; %% Styling

&nbsp; classDef unobserved fill:#ffcccc,stroke:#ff6666,stroke-width:2px

&nbsp; classDef treatment fill:#ccffcc,stroke:#66cc66,stroke-width:3px

&nbsp; classDef outcome fill:#ccccff,stroke:#6666cc,stroke-width:2px

&nbsp; classDef confounder fill:#ffffcc,stroke:#cccc66,stroke-width:2px

&nbsp; classDef mechanism fill:#ffeecc,stroke:#cc9966,stroke-width:1px



&nbsp; class CQ,CC unobserved

&nbsp; class AS,PR treatment

&nbsp; class DT,Cost,OT,Sat outcome

&nbsp; class CS,T,SL confounder

&nbsp; class CarrierSel,SR mechanism

```

