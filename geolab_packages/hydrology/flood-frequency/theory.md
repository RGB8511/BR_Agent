# Flood Frequency Analysis

## Purpose

Flood frequency analysis estimates the probability of flood events of various magnitudes. It answers questions like: What is the 100-year flood discharge? What is the probability a given flood magnitude will be exceeded in the next 50 years? This is the foundation for floodplain mapping, dam design, culvert sizing, and insurance programs.

## Data Sources and Types

### Annual Maximum Series (AMS)
The largest peak flow in each water year. Standard approach for Bulletin 17C. Simple but discards the second-largest flood even if it exceeds the largest flood in other years.

### Partial Duration Series (PDS) / Peaks Over Threshold (POT)
All peaks above a selected threshold. Captures more events. For return periods > 10 years, AMS and PDS give nearly identical results. PDS is preferred for shorter return periods (2–10 years).

### Gauge Data
USGS stream gauges provide the primary data. Systematic record (continuous gauge operation) is distinguished from historical information (knowledge of specific large events outside the systematic record).

## Log-Pearson Type III Distribution (Bulletin 17C)

The standard distribution for flood frequency analysis in the United States.

### Procedure
1. Take the logarithms of the annual maximum series: X = log(Q)
2. Compute sample statistics: mean (X̄), standard deviation (s), skew coefficient (G)
3. Compute the flood quantile: log(Q_T) = X̄ + K_T × s

where K_T is the frequency factor from the LP-III distribution, dependent on skew (G) and return period (T).

### Skew Coefficient
The skew coefficient G controls the shape of the LP-III distribution. Station skew (computed from data) is noisy for short records. Bulletin 17C recommends a weighted skew:

G_w = (MSE_G × G_R + MSE_R × G_s) / (MSE_G + MSE_R)

where G_s = station skew, G_R = regional skew (from USGS skew map), MSE = mean square error of each estimate.

### Expected Moments Algorithm (EMA)
Bulletin 17C replaces the older method-of-moments with the Expected Moments Algorithm (EMA), which properly handles:
- **Censored data:** Flows known only to be above or below a threshold (e.g., perception thresholds for historical floods)
- **Historical information:** Large floods known to have occurred before the systematic record
- **Potentially influential low floods (PILFs):** Outliers on the low end that distort the fitted distribution — handled by the Multiple Grubbs-Beck (MGB) test

## Other Distributions

### Gumbel (EV Type I)
Q_T = μ + (σ_x / σ_n) × (y_T - ȳ_n)

Special case of LP-III with skew = 1.1396. Commonly used internationally. Two-parameter distribution — simpler but less flexible than LP-III.

### Generalized Extreme Value (GEV)
Three-parameter distribution that includes Gumbel (shape k=0), Fréchet (k>0), and Weibull (k<0) as special cases. Standard in UK (Flood Estimation Handbook) and many international applications. Fitted by L-moments or maximum likelihood.

### Log-Normal
Two or three-parameter log-normal. Equivalent to LP-III with skew = 0. Sometimes used for regional analysis or as a check.

## Plotting Positions

To plot observed data on probability paper, each observation is assigned a plotting position:

p_i = (i - a) / (n + 1 - 2a)

where i = rank (1 = smallest), n = sample size, and a varies by formula:
- Weibull: a = 0 → p = i/(n+1) — most common for flood frequency
- Cunnane: a = 0.40 — recommended by many statisticians
- Hazen: a = 0.50 → p = (i-0.5)/n

Return period: T = 1/p for annual exceedance probability (use T = 1/(1-p) if p is non-exceedance).

## Confidence Intervals

Flood quantile estimates have uncertainty. Approximate confidence limits for LP-III:

Q_upper = exp(X̄ + K_upper × s)
Q_lower = exp(X̄ + K_lower × s)

where K values incorporate both sampling error in mean and variance. Width of confidence interval depends on record length, skew, and return period. Longer records → narrower intervals.

## Regional Regression Equations

For ungauged sites, regional regression equations estimate flood quantiles from watershed characteristics:

Q_T = a × A^b × S^c × P^d × ...

where A = drainage area, S = slope, P = mean annual precipitation. Developed by USGS for each state/region (e.g., StreamStats web application). Provide estimates with associated prediction intervals.

## Stationarity and Climate

Traditional frequency analysis assumes stationarity — the statistical properties of floods don't change over time. Climate change, urbanization, and land use change may violate this assumption. Non-stationary methods (time-varying parameters) are an active research area but not yet standard practice.
