```mermaid
graph TD
    Treatment[🔄 Logistics System]
    Cost[💵 Cost per Shipment]

    %% Confounders
    PackageWeight[⚖️ Weight]
    ServiceLevel[🚀 Service Level]
    Distance[🗺️ Distance]
    FuelPrice[⛽ Fuel Price]
    PeakSeason[📈 Peak Season]
    MonthlyVolume[📦 Volume]

    %% Collider (avoid)
    Performance[⭐ Performance Rating]

    %% Arrows
    Treatment --> Cost
    PackageWeight --> Cost
    ServiceLevel --> Cost
    Distance --> Cost
    FuelPrice --> Cost
    PeakSeason --> Cost
    MonthlyVolume --> Cost

    %% Collider Path
    Treatment --> Performance
    Cost --> Performance
```

```mermaid
graph TD
    Treatment[🔄 Logistics System]
    Time[⏱️ Delivery Time]

    %% Confounders
    ServiceLevel[🚀 Service Level]
    Distance[🗺️ Distance]
    PackageWeight[⚖️ Weight]
    Weather[🌧️ Weather]
    Holiday[🎄 Holiday]
    PeakSeason[📈 Peak Season]

    %% Collider (avoid)
    Performance[⭐ Performance Rating]

    %% Arrows
    Treatment --> Time
    ServiceLevel --> Time
    Distance --> Time
    PackageWeight --> Time
    Weather --> Time
    Holiday --> Time
    PeakSeason --> Time

    %% Collider Path
    Treatment --> Performance
    Time --> Performance
```
