# RUBRICS: API Design Pattern Usability Analysis

This document defines the evaluation criteria for all three questions in the API Design Pattern Usability Analysis task.

---

## Question 1: Cognitive Dimension Violation Cost Analysis

### Complete Question Text
Quantify the cognitive usability cost of the factory pattern by determining how many dimensions from Clarke & Becker's framework are violated based on Ellis et al.'s empirical observations, then calculate a per-dimension time penalty coefficient. From Ellis, extract the factory pattern's time penalty ratio for the SSLSocket task, count total dimension violations, and divide the time penalty by violation count to derive a normalized per-dimension cost coefficient. Compare this to the helper class methods pattern by extracting speedup ratios across Stylos & Myers's three experimental tasks, calculating the average speedup, and computing its per-dimension coefficient using the same normalization approach. Calculate the ratio between the two coefficients to determine which API design pattern imposes greater cognitive cost per violated dimension.

---

CRITERION 1 [Accuracy]
Description: Identifies "5" as the number of cognitive dimensions the factory pattern violates
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Ellis et al. 2007 - Factory Pattern Usability Problems):
"Problem 1: Finding the Factory - All participants expected constructors to exist... 6/12 participants (50%) believed they needed to create subclasses"
"Problem 2: Abstract Factory Complexity - Factory itself is abstract class, requiring factory method to obtain instance"
"Problem 3: Return Type Covariance Issues - SSLSocketFactory.getDefault() returns SocketFactory (superclass type)... Participants uncertain if returned object was actually SSLSocketFactory"
"Problem 6: Documentation Placement - Critical information buried at bottom of long class descriptions... Most found factory only by lexical proximity in class list"
"Problem 7: Treating Factories as Constructors - 5/12 participants called factory methods and ignored return value"

Source 2 (Clarke & Becker 2003 - Cognitive Dimensions Framework):
1. **Work-Step Unit** - "How much does a user have to do to accomplish a single goal?" Factory requires: find factory class → obtain factory instance → invoke factory method → use product. Constructor requires: invoke constructor → use object.
2. **Penetrability** - "How easy is it to understand what is happening inside?" Factory pattern hides instantiation mechanism; documentation doesn't explain why constructors are disabled.
3. **Premature Commitment** - "To what extent does a developer have to make decisions before all the needed information is available?" Must discover factory pattern before attempting instantiation.
4. **Abstraction Gradient** - "What is the minimum and maximum levels of abstraction?" Adds factory abstraction layer between developer and product.
5. **Hidden Dependencies** - "Are dependencies between entities visible or hidden?" Requires discovering SSLSocketFactory class; dependency not obvious from SSLSocket.

The factory pattern violates 5 cognitive dimensions from Clarke & Becker's framework based on Ellis's empirical observations.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf, http://www.ppig.org/sites/default/files/2003-PPIG-15th-clarke.pdf

CRITERION 2 [Accuracy]
Description: Calculates "0.42" as the factory pattern's per-dimension time penalty coefficient
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (Ellis et al. 2007, Task 2: Sockets Task — time penalty ratio):
"SSLSocket (Factory): Median = 16:05 (965 seconds)"
"MulticastSocket (Constructor): Median = 7:41 (461 seconds)"
Factory time penalty ratio: 965 ÷ 461 = 2.093 ≈ 2.09

Source 2 (Ellis et al. 2007 usability problems mapped to Clarke & Becker 2003 — dimension violations):
1. Work-Step Unit (find factory → obtain instance → invoke method → use product)
2. Penetrability (instantiation mechanism hidden, not obvious from SSLSocket)
3. Premature Commitment (must discover factory pattern before attempting instantiation)
4. Abstraction Gradient (adds factory abstraction layer between developer and product)
5. Hidden Dependencies (requires finding SSLSocketFactory class — dependency not obvious from SSLSocket)
Factory dimension violations: 5

Calculation: 2.09 ÷ 5 = 0.418 ≈ 0.42
The per-dimension coefficient normalizes the time penalty by the number of violated dimensions, giving 0.42 as the cognitive cost per dimension for the factory pattern.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf, http://www.ppig.org/sites/default/files/2003-PPIG-15th-clarke.pdf

CRITERION 3 [Accuracy]
Description: Identifies "965" as Ellis's SSLSocket factory pattern median completion time in seconds
Weight: Critical
Numerical Weight: 5
Rationale: Source (Ellis et al. 2007, Task 2: Sockets Task):
"SSLSocket (Factory): Mean time = 20:05 (1205 seconds), SD = 11:17, Median = 16:05"
Conversion: 16 minutes × 60 seconds + 5 seconds = 960 + 5 = 965 seconds
The SSLSocket task using the factory pattern had a median completion time of 16:05, which equals 965 seconds.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

CRITERION 4 [Accuracy]
Description: Identifies "461" as Ellis's SSLSocket constructor baseline median completion time in seconds
Weight: Critical
Numerical Weight: 5
Rationale: Source (Ellis et al. 2007, Task 2: Sockets Task):
"MulticastSocket (Constructor): Mean time = 9:31 (571 seconds), SD = 8:04, Median = 7:41"
Conversion: 7 minutes × 60 seconds + 41 seconds = 420 + 41 = 461 seconds
The MulticastSocket task using the constructor pattern (baseline) had a median completion time of 7:41, which equals 461 seconds.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

CRITERION 5 [Accuracy]
Description: Calculates "2.09" as the factory pattern's time penalty ratio for the SSLSocket task
Weight: Critical
Numerical Weight: 5
Rationale: Source (Ellis et al. 2007, Task 2: Sockets Task):
"SSLSocket (Factory): Mean time = 20:05 (1205 seconds), SD = 11:17, Median = 16:05"
SSLSocket factory median time: 16 minutes × 60 + 5 seconds = 965 seconds

"MulticastSocket (Constructor): Mean time = 9:31 (571 seconds), SD = 8:04, Median = 7:41"
SSLSocket constructor baseline median time: 7 minutes × 60 + 41 seconds = 461 seconds

Calculation: 965 ÷ 461 = 2.093 ≈ 2.09
The factory pattern imposed a 2.09× time penalty compared to the constructor baseline in Ellis's SSLSocket task.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

CRITERION 6 [Accuracy]
Description: Identifies "Email" as the first task name in Stylos & Myers's method placement study
Weight: Major
Numerical Weight: 4
Rationale: Source (Stylos & Myers 2008, Experimental Design):
"Task 1: Email task - Sending an email message using JavaMail API"
"Median Time - Starting Class: 1.0 min, Helper Class: 11.2 min"
The first experimental task was the Email task, which required participants to send an email using the JavaMail API.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 7 [Accuracy]
Description: Identifies "Web" as the second task name in Stylos & Myers's method placement study
Weight: Major
Numerical Weight: 4
Rationale: Source (Stylos & Myers 2008, Experimental Design):
"Task 2: Web task - Fetching web page content"
"Median Time - Starting Class: 2.0 min, Helper Class: 15.2 min"
The second experimental task was the Web task, which required participants to fetch web page content.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 8 [Accuracy]
Description: Identifies "Thingies" as the third task name in Stylos & Myers's method placement study
Weight: Major
Numerical Weight: 4
Rationale: Source (Stylos & Myers 2008, Experimental Design):
"Task 3: Thingies task - Database-related task"
"Median Time - Starting Class: 2.8 min, Helper Class: 6.8 min"
The third experimental task was the Thingies task, which was a database-related programming task.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 9 [Accuracy]
Description: Calculates "11.2" as the Email task speedup ratio (helper class penalty)
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Myers 2008, Table 1 - Email Task Results):
"Starting Class Methods: Median = 1.0 minute"
"Helper Class Methods: Median = 11.2 minutes"
Calculation: 11.2 minutes ÷ 1.0 minute = 11.2
The Email task showed an 11.2× speedup ratio, meaning helper class methods took 11.2 times longer than starting class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 10 [Accuracy]
Description: Calculates "7.6" as the Web task speedup ratio (helper class penalty)
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Myers 2008, Table 1 - Web Task Results):
"Starting Class Methods: Median = 2.0 minutes"
"Helper Class Methods: Median = 15.2 minutes"
Calculation: 15.2 minutes ÷ 2.0 minutes = 7.6
The Web task showed a 7.6× speedup ratio, meaning helper class methods took 7.6 times longer than starting class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 11 [Accuracy]
Description: Calculates "2.4" as the Thingies task speedup ratio (helper class penalty)
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Myers 2008, Table 1 - Thingies Task Results):
"Starting Class Methods: Median = 2.8 minutes"
"Helper Class Methods: Median = 6.8 minutes"
Calculation: 6.8 minutes ÷ 2.8 minutes = 2.428... ≈ 2.4
The Thingies task showed a 2.4× speedup ratio, meaning helper class methods took 2.4 times longer than starting class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 12 [Accuracy]
Description: Calculates "7.07" as the average speedup ratio across all three tasks
Weight: Major
Numerical Weight: 4
Rationale: Source (Stylos & Myers 2008, Table 1 — all three tasks):
Email task: Starting Class Median = 1.0 minute, Helper Class Median = 11.2 minutes → speedup = 11.2 ÷ 1.0 = 11.2
Web task: Starting Class Median = 2.0 minutes, Helper Class Median = 15.2 minutes → speedup = 15.2 ÷ 2.0 = 7.6
Thingies task: Starting Class Median = 2.8 minutes, Helper Class Median = 6.8 minutes → speedup = 6.8 ÷ 2.8 = 2.4

Calculation: (11.2 + 7.6 + 2.4) ÷ 3 = 21.2 ÷ 3 = 7.0666... ≈ 7.07
The average speedup ratio across all three experimental tasks is 7.07, representing the typical time penalty for helper class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 13 [Accuracy]
Description: Calculates "2.36" as the helper class pattern's per-dimension time penalty coefficient
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (Stylos & Myers 2008, Table 1 — average speedup across all three tasks):
Email task: Starting Class Median = 1.0 minute, Helper Class Median = 11.2 minutes → speedup = 11.2 ÷ 1.0 = 11.2
Web task: Starting Class Median = 2.0 minutes, Helper Class Median = 15.2 minutes → speedup = 15.2 ÷ 2.0 = 7.6
Thingies task: Starting Class Median = 2.8 minutes, Helper Class Median = 6.8 minutes → speedup = 6.8 ÷ 2.8 = 2.4
Average speedup: (11.2 + 7.6 + 2.4) ÷ 3 = 21.2 ÷ 3 = 7.07

Source 2 (Stylos & Myers 2008 findings mapped to Clarke & Becker 2003 framework — dimension violations):
1. **Work-Step Unit** - Must find helper class → navigate to it → use it (multi-step process)
2. **Penetrability** - Helper classes not discoverable from starting class (Transport, HttpTransportProperties.Authenticator hidden)
3. **Working Framework** - Must track relationships between multiple classes (starting class + helper class architecture)
Total violations: 3

Calculation: 7.07 ÷ 3 = 2.356... ≈ 2.36
The per-dimension coefficient for helper class methods is 2.36, representing the cognitive cost per violated dimension.
Sources: https://doi.org/10.1145/1453101.1453117, http://www.ppig.org/sites/default/files/2003-PPIG-15th-clarke.pdf

CRITERION 14 [Accuracy]
Description: Calculates "5.6" as the coefficient ratio between helper class and factory patterns
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (Stylos & Myers 2008 — helper class per-dimension coefficient derivation):
Email task speedup: 11.2 ÷ 1.0 = 11.2; Web task speedup: 15.2 ÷ 2.0 = 7.6; Thingies task speedup: 6.8 ÷ 2.8 = 2.4
Average speedup: (11.2 + 7.6 + 2.4) ÷ 3 = 7.07
Helper class violations (Work-Step Unit, Penetrability, Working Framework): 3
Helper class per-dimension coefficient: 7.07 ÷ 3 = 2.36

Source 2 (Ellis et al. 2007 — factory per-dimension coefficient derivation):
Factory time penalty ratio: 965 ÷ 461 = 2.09 (SSLSocket factory median 965s vs constructor baseline 461s)
Factory violations (Work-Step Unit, Penetrability, Premature Commitment, Abstraction Gradient, Hidden Dependencies): 5
Factory per-dimension coefficient: 2.09 ÷ 5 = 0.42

Calculation: 2.36 ÷ 0.42 = 5.619... ≈ 5.6
The coefficient ratio is 5.6, meaning helper class methods impose 5.6 times more cognitive cost per violated dimension than factory patterns.
Sources: https://doi.org/10.1145/1453101.1453117, http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

CRITERION 15 [Accuracy]
Description: Identifies "Helper class" as the API design pattern with greater cognitive cost per violated dimension
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Stylos & Myers 2008 — helper class per-dimension coefficient derivation):
Email task speedup: 11.2 ÷ 1.0 = 11.2; Web task speedup: 15.2 ÷ 2.0 = 7.6; Thingies task speedup: 6.8 ÷ 2.8 = 2.4
Average speedup: (11.2 + 7.6 + 2.4) ÷ 3 = 7.07
Helper class violations (Work-Step Unit, Penetrability, Working Framework): 3
Helper class per-dimension coefficient: 7.07 ÷ 3 = 2.36

Source 2 (Ellis et al. 2007 — factory per-dimension coefficient derivation):
Factory time penalty ratio: 965 ÷ 461 = 2.09 (SSLSocket factory median 965s vs constructor baseline 461s)
Factory violations (Work-Step Unit, Penetrability, Premature Commitment, Abstraction Gradient, Hidden Dependencies): 5
Factory per-dimension coefficient: 2.09 ÷ 5 = 0.42

Comparison: 2.36 > 0.42
Coefficient ratio: 2.36 ÷ 0.42 = 5.6
Helper class methods impose 5.6 times greater cognitive cost per violated dimension than factory patterns (2.36 vs 0.42), making them the pattern with higher per-dimension cognitive burden.
Sources: https://doi.org/10.1145/1453101.1453117, http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

---

## Question 2: Experience-Adjusted Pattern Complexity Score

### Complete Question Text
Synthesize findings across studies to derive an experience-adjusted API pattern complexity metric by extracting the percentage improvement in task completion time for experienced versus less experienced developers on complex tasks from Piccioni et al., calculating the average speedup ratio between starting class methods and helper class methods across Stylos & Myers's three experimental tasks, and applying Piccioni's experience benefit percentage to adjust this average speedup to derive an Experience-Adjusted Method Placement Penalty. Compare this experience-adjusted penalty to Ellis's factory pattern time penalty ratio for the SSLSocket task and calculate the ratio to determine which API design approach imposes greater cognitive cost even after accounting for developer experience.

---

CRITERION 16 [Accuracy]
Description: Identifies "45%" as the percentage improvement in task completion time for experienced developers
Weight: Critical
Numerical Weight: 5
Rationale: Source (Piccioni et al. 2013, Developer Experience Analysis):
"Developers with 5+ years of experience completed complex API tasks 45% faster than developers with less than 5 years of experience"
"Experience Effect: The data shows a clear benefit of experience on complex tasks, with a 45% time reduction for experienced developers"
Interpretation: Experienced developers (5+ years) complete tasks in 55% of the time that less experienced developers require (100% - 45% = 55%).
Sources: https://se.inf.ethz.ch/~meyer/publications/empirical/API_usability.pdf

CRITERION 17 [Accuracy]
Description: Identifies "11.2" as the Email task speedup ratio
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Myers 2008, Table 1 - Email Task Results):
"Starting Class Methods: Median = 1.0 minute"
"Helper Class Methods: Median = 11.2 minutes"
Calculation: 11.2 ÷ 1.0 = 11.2
The Email task shows helper class methods took 11.2 times longer than starting class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 18 [Accuracy]
Description: Identifies "7.6" as the Web task speedup ratio
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Myers 2008, Table 1 - Web Task Results):
"Starting Class Methods: Median = 2.0 minutes"
"Helper Class Methods: Median = 15.2 minutes"
Calculation: 15.2 ÷ 2.0 = 7.6
The Web task shows helper class methods took 7.6 times longer than starting class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 19 [Accuracy]
Description: Identifies "2.4" as the Thingies task speedup ratio
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Myers 2008, Table 1 - Thingies Task Results):
"Starting Class Methods: Median = 2.8 minutes"
"Helper Class Methods: Median = 6.8 minutes"
Calculation: 6.8 ÷ 2.8 = 2.428... ≈ 2.4
The Thingies task shows helper class methods took 2.4 times longer than starting class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 20 [Accuracy]
Description: Calculates "21.2" as the sum of the three task speedup ratios
Weight: Major
Numerical Weight: 4
Rationale: Source (Stylos & Myers 2008, Table 1 — all three tasks):
Email task: Starting Class Median = 1.0 minute, Helper Class Median = 11.2 minutes → speedup = 11.2 ÷ 1.0 = 11.2
Web task: Starting Class Median = 2.0 minutes, Helper Class Median = 15.2 minutes → speedup = 15.2 ÷ 2.0 = 7.6
Thingies task: Starting Class Median = 2.8 minutes, Helper Class Median = 6.8 minutes → speedup = 6.8 ÷ 2.8 = 2.4

Calculation: 11.2 + 7.6 + 2.4 = 21.2
The sum of all three speedup ratios is 21.2, which is used to calculate the average speedup.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 21 [Accuracy]
Description: Calculates "7.07" as the average speedup ratio across all three tasks
Weight: Major
Numerical Weight: 4
Rationale: Source (Stylos & Myers 2008, Table 1 — all three tasks):
Email task: Starting Class Median = 1.0 minute, Helper Class Median = 11.2 minutes → speedup = 11.2 ÷ 1.0 = 11.2
Web task: Starting Class Median = 2.0 minutes, Helper Class Median = 15.2 minutes → speedup = 15.2 ÷ 2.0 = 7.6
Thingies task: Starting Class Median = 2.8 minutes, Helper Class Median = 6.8 minutes → speedup = 6.8 ÷ 2.8 = 2.4

Sum: 11.2 + 7.6 + 2.4 = 21.2
Calculation: 21.2 ÷ 3 = 7.0666... ≈ 7.07
The average speedup ratio across all three experimental tasks is 7.07, representing the typical time penalty for helper class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 22 [Accuracy]
Description: Calculates "0.55" as the complement of the 45% experience improvement
Weight: Major
Numerical Weight: 4
Rationale: Source (Piccioni et al. 2013, Developer Experience Analysis):
"Developers with 5+ years of experience completed complex API tasks 45% faster than developers with less than 5 years of experience"
Experience improvement percentage: 45% = 0.45

Complement calculation: 1 - 0.45 = 0.55
Interpretation: If experienced developers are 45% faster, they complete tasks in 55% of the original time. The complement (0.55) represents the fraction of time experienced developers require compared to less experienced developers.
Sources: https://se.inf.ethz.ch/~meyer/publications/empirical/API_usability.pdf

CRITERION 23 [Accuracy]
Description: Calculates "3.89" as the Experience-Adjusted Method Placement Penalty
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Stylos & Myers 2008, Table 1 — average speedup derivation):
Email task: 11.2 ÷ 1.0 = 11.2; Web task: 15.2 ÷ 2.0 = 7.6; Thingies task: 6.8 ÷ 2.8 = 2.4
Average speedup: (11.2 + 7.6 + 2.4) ÷ 3 = 21.2 ÷ 3 = 7.07

Source 2 (Piccioni et al. 2013 — experience adjustment factor derivation):
"Developers with 5+ years of experience completed complex API tasks 45% faster than developers with less than 5 years of experience"
Experience improvement: 45% = 0.45; complement (adjustment factor): 1 - 0.45 = 0.55

Calculation: 7.07 × 0.55 = 3.8885 ≈ 3.89
Formula: Experience-Adjusted Penalty = Average_Speedup × (1 - Experience_Benefit_Percentage)
Interpretation: Even when accounting for the 45% benefit that experienced developers gain on complex tasks, helper class methods still impose a 3.89× time penalty. This adjusted metric isolates the API design's inherent complexity from the effect of developer experience.
Sources: https://doi.org/10.1145/1453101.1453117, https://se.inf.ethz.ch/~meyer/publications/empirical/API_usability.pdf

CRITERION 24 [Accuracy]
Description: Identifies "2.09" as Ellis's factory pattern time penalty ratio
Weight: Critical
Numerical Weight: 5
Rationale: Source (Ellis et al. 2007, Task 2: Sockets Task):
"SSLSocket (Factory): Mean time = 20:05 (1205 seconds), SD = 11:17, Median = 16:05"
SSLSocket factory median time: 16 minutes × 60 + 5 seconds = 965 seconds

"MulticastSocket (Constructor): Mean time = 9:31 (571 seconds), SD = 8:04, Median = 7:41"
Constructor baseline median time: 7 minutes × 60 + 41 seconds = 461 seconds

Calculation: 965 ÷ 461 = 2.093 ≈ 2.09
The factory pattern imposed a 2.09× time penalty compared to the constructor baseline in Ellis's SSLSocket task.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

CRITERION 25 [Accuracy]
Description: Identifies "Helper class" as the API design approach with greater cognitive cost after experience adjustment
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Stylos & Myers 2008 + Piccioni et al. 2013 — Experience-Adjusted Method Placement Penalty):
Email task speedup: 11.2 ÷ 1.0 = 11.2; Web task speedup: 15.2 ÷ 2.0 = 7.6; Thingies task speedup: 6.8 ÷ 2.8 = 2.4
Average speedup: (11.2 + 7.6 + 2.4) ÷ 3 = 7.07
Piccioni experience improvement: 45% → adjustment factor = 1 - 0.45 = 0.55
Experience-Adjusted Method Placement Penalty: 7.07 × 0.55 = 3.89

Source 2 (Ellis et al. 2007, Task 2: Sockets Task — factory time penalty):
SSLSocket factory median: 16:05 = 965 seconds; Constructor baseline median: 7:41 = 461 seconds
Factory pattern time penalty ratio: 965 ÷ 461 = 2.09

Comparison: 3.89 > 2.09
Even after accounting for developer experience (45% improvement for experienced developers), helper class methods impose a 3.89× time penalty, which is still greater than the factory pattern's 2.09× penalty. This indicates that helper class methods impose greater cognitive cost than factory patterns, regardless of developer experience level.
Sources: https://doi.org/10.1145/1453101.1453117, https://se.inf.ethz.ch/~meyer/publications/empirical/API_usability.pdf, http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

CRITERION 26 [Accuracy]
Description: Calculates "1.86" as the ratio between experience-adjusted helper penalty and factory penalty
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (Stylos & Myers 2008 + Piccioni et al. 2013 — Experience-Adjusted Method Placement Penalty):
Email task speedup: 11.2 ÷ 1.0 = 11.2; Web task speedup: 15.2 ÷ 2.0 = 7.6; Thingies task speedup: 6.8 ÷ 2.8 = 2.4
Average speedup: (11.2 + 7.6 + 2.4) ÷ 3 = 7.07
Piccioni experience improvement: 45% → adjustment factor = 1 - 0.45 = 0.55
Experience-Adjusted Method Placement Penalty: 7.07 × 0.55 = 3.89

Source 2 (Ellis et al. 2007, Task 2: Sockets Task — factory time penalty):
SSLSocket factory median: 16:05 = 965 seconds; Constructor baseline median: 7:41 = 461 seconds
Factory pattern time penalty ratio: 965 ÷ 461 = 2.09

Calculation: 3.89 ÷ 2.09 = 1.861... ≈ 1.86
Interpretation: The experience-adjusted method placement penalty (3.89×) is 1.86 times larger than the factory pattern penalty (2.09×). This means that even when experienced developers benefit from their expertise (45% faster), helper class methods still impose 1.86 times more cognitive burden than factory patterns.
Sources: https://doi.org/10.1145/1453101.1453117, https://se.inf.ethz.ch/~meyer/publications/empirical/API_usability.pdf, http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

---

## Question 3: Cross-Study API Pattern Comparison Table

### Complete Question Text
Create an image of a table comparing API design patterns across the empirical studies with exactly 3 data rows (excluding header) and exactly 3 columns. The table must have the exact title: "API Design Pattern Usability: Empirical Evidence Synthesis". Column headers must be: "Pattern", "Time Penalty (vs. Baseline)", "Cognitive Violations". Row 1 must be labeled "Factory Pattern" and contain Ellis's SSLSocket data (time penalty as ratio, number of Clarke dimensions violated). Row 2 must be labeled "Required Constructor Parameters" and contain Stylos & Clarke's data (comparing to create-set-call baseline, number of violated dimensions). Row 3 must be labeled "Helper Class Methods" and contain Stylos & Myers's Email task data (time penalty ratio, number of violated dimensions).

---

CRITERION 27 [Table Structure]
Description: Outputs the comparison in a table format
Weight: Critical
Numerical Weight: 5
Rationale: The prompt explicitly requests: "Create an image of a table comparing API design patterns across the empirical studies". The response must present the comparison as a properly formatted markdown table with pipe delimiters and header separators to be considered valid for image generation.
Sources: Prompt

CRITERION 28 [Table Structure]
Description: Formats the table with 3 columns
Weight: Critical
Numerical Weight: 5
Rationale: The prompt specifies: "exactly 3 columns". The table must have three columns: (1) "Pattern", (2) "Time Penalty (vs. Baseline)", and (3) "Cognitive Violations". A table with fewer or more columns fails to meet the specification.
Sources: Prompt

CRITERION 29 [Table Structure]
Description: Formats the table with 3 data rows (excluding header)
Weight: Critical
Numerical Weight: 5
Rationale: The prompt specifies: "exactly 3 data rows (excluding header)". The table must have exactly 3 data rows for: (1) Factory Pattern, (2) Required Constructor Parameters, and (3) Helper Class Methods. More or fewer rows indicates incorrect content.
Sources: Prompt

CRITERION 30 [Table Structure]
Description: Includes "API Design Pattern Usability: Empirical Evidence Synthesis" as the table title
Weight: Major
Numerical Weight: 4
Rationale: The prompt explicitly specifies: "The table must have the exact title: 'API Design Pattern Usability: Empirical Evidence Synthesis'". The title provides context for the cross-study comparison and should appear immediately before the table.
Expected golden output:
API Design Pattern Usability: Empirical Evidence Synthesis

| Pattern | Time Penalty (vs. Baseline) | Cognitive Violations |
| --- | --- | --- |
| Factory Pattern | 2.09 | 5 |
| Required Constructor Parameters | N/A | 3 |
| Helper Class Methods | 11.2 | 3 |
Sources: Prompt

CRITERION 31 [Table Content]
Description: Includes "Pattern" as the first column header
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies column headers must include "Pattern" as the first column to identify each API design pattern being compared.
Sources: Prompt

CRITERION 32 [Table Content]
Description: Includes "Time Penalty (vs. Baseline)" as the second column header
Weight: Major
Numerical Weight: 4
Rationale: The prompt explicitly specifies: "Column headers must be: 'Pattern', 'Time Penalty (vs. Baseline)', 'Cognitive Violations'". The second column header must be "Time Penalty (vs. Baseline)" to show the empirical performance cost of each pattern.
Sources: Prompt

CRITERION 33 [Table Content]
Description: Includes "Cognitive Violations" as the third column header
Weight: Major
Numerical Weight: 4
Rationale: The prompt explicitly specifies: "Column headers must be: 'Pattern', 'Time Penalty (vs. Baseline)', 'Cognitive Violations'". The third column header must be "Cognitive Violations" to show how many dimensions from Clarke & Becker's framework each pattern violates.
Sources: Prompt

CRITERION 34 [Table Content]
Description: Includes "Factory Pattern" as Row 1 pattern name
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies: "Row 1 must be labeled 'Factory Pattern'". This identifies the factory design pattern in the comparison table.
Sources: Prompt

CRITERION 35 [Table Content]
Description: Includes "2.09" as the factory pattern's time penalty value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (Ellis et al. 2007, Task 2: Sockets Task):
"SSLSocket (Factory): Median = 16:05 (965 seconds)"
"MulticastSocket (Constructor): Median = 7:41 (461 seconds)"
Calculation: 965 ÷ 461 = 2.093 ≈ 2.09
The table cell for Row 1's "Time Penalty (vs. Baseline)" column must contain the value 2.09 (or 2.09×), representing Ellis's SSLSocket factory pattern time penalty compared to the constructor baseline.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

CRITERION 36 [Table Content]
Description: Includes "5" as the factory pattern's cognitive violations count in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Ellis et al. 2007 — empirical usability problems observed):
"Problem 1: Finding the Factory - All participants expected constructors to exist... 6/12 participants (50%) believed they needed to create subclasses"
"Problem 2: Abstract Factory Complexity - Factory itself is abstract class, requiring factory method to obtain instance"
"Problem 3: Return Type Covariance Issues - SSLSocketFactory.getDefault() returns SocketFactory (superclass type)... Participants uncertain if returned object was actually SSLSocketFactory"
"Problem 6: Documentation Placement - Critical information buried at bottom of long class descriptions"
"Problem 7: Treating Factories as Constructors - 5/12 participants called factory methods and ignored return value"

Source 2 (Clarke & Becker 2003 — Cognitive Dimensions Framework mapping):
1. Work-Step Unit — factory requires: find factory class → obtain factory instance → invoke factory method → use product (vs. constructor: invoke → use)
2. Penetrability — factory pattern hides instantiation mechanism; documentation doesn't explain why constructors are disabled
3. Premature Commitment — must discover factory pattern before attempting instantiation
4. Abstraction Gradient — adds factory abstraction layer between developer and product
5. Hidden Dependencies — requires discovering SSLSocketFactory class; dependency not obvious from SSLSocket

The table cell for Row 1's "Cognitive Violations" column must contain the value 5.
Sources: http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf, http://www.ppig.org/sites/default/files/2003-PPIG-15th-clarke.pdf

CRITERION 37 [Table Content]
Description: Includes "Required Constructor Parameters" as Row 2 pattern name
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies: "Row 2 must be labeled 'Required Constructor Parameters'". This identifies the required constructor parameters API design pattern.
Sources: Prompt

CRITERION 38 [Table Content]
Description: Includes "N/A" (or similar indicator) as the required constructor parameters time penalty value
Weight: Major
Numerical Weight: 4
Rationale: Source (Stylos & Clarke 2007):
"Result: 30/30 participants (100%) used create-set-call in their imagined code"
"The study focused on avoidance behavior and preference patterns, not completion time comparisons"
Stylos & Clarke (2007) did not measure time penalties; they measured avoidance behavior. 100% of participants avoided required constructor parameters in favor of create-set-call pattern, but no time penalty data is available. The table should indicate "N/A", "Not measured", or similar.
Sources: http://www.cs.cmu.edu/afs/cs/Web/People/marmalade/papers/Stylos2007CreateSetCall.pdf

CRITERION 39 [Table Content]
Description: Includes "3" as the required constructor parameters cognitive violations count
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Clarke 2007 findings mapped to Clarke & Becker 2003 framework):
1. **Premature Commitment** - "Developers must know parameter values before exploring the API... forces upfront decisions before sufficient information is available"
2. **Viscosity** - "Once parameters are set in constructor, changing them requires creating a new object... high cost of change"
3. **Visibility** - "Required parameters not easily discoverable... developers must read documentation to know what parameters are needed"
The table cell for Row 2's "Cognitive Violations" column must contain the value 3.
Sources: http://www.cs.cmu.edu/afs/cs/Web/People/marmalade/papers/Stylos2007CreateSetCall.pdf, http://www.ppig.org/sites/default/files/2003-PPIG-15th-clarke.pdf

CRITERION 40 [Table Content]
Description: Includes "Helper Class Methods" as Row 3 pattern name
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies: "Row 3 must be labeled 'Helper Class Methods'". This identifies the helper class methods API design pattern.
Sources: Prompt

CRITERION 41 [Table Content]
Description: Includes "11.2" as the helper class methods time penalty value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (Stylos & Myers 2008, Table 1 - Email Task Results):
"Starting Class Methods: Median = 1.0 minute"
"Helper Class Methods: Median = 11.2 minutes"
Calculation: 11.2 ÷ 1.0 = 11.2
The prompt specifies: "Row 3 must... contain Stylos & Myers's Email task data (time penalty ratio...)". The table cell for Row 3's "Time Penalty (vs. Baseline)" column must contain 11.2 (or 11.2×), representing the Email task time penalty for helper class methods.
Sources: https://doi.org/10.1145/1453101.1453117

CRITERION 42 [Table Content]
Description: Includes "3" as the helper class methods cognitive violations count in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Stylos & Myers 2008 — empirical findings on helper class placement):
"Participants using the helper class API had significantly longer task completion times across all three tasks"
"Task 1 (Email): Helper class methods (Transport, Session.getInstance, etc.) were difficult to discover from the starting class (Message/MimeMessage)"
"The helper classes were in separate packages or required additional navigation beyond the starting class"

Source 2 (Clarke & Becker 2003 — Cognitive Dimensions Framework mapping):
1. **Work-Step Unit** — multi-step process: find helper class → navigate to it → use its methods (e.g., Transport, HttpTransportProperties.Authenticator) rather than using methods on the starting class directly
2. **Penetrability** — helper classes not discoverable from starting class; hidden in separate packages or class hierarchies not visible from the entry point
3. **Working Framework** — must track relationships between multiple classes; adds architectural complexity (starting class + helper class structure) that must be held in working memory

The table cell for Row 3's "Cognitive Violations" column must contain the value 3.
Sources: https://doi.org/10.1145/1453101.1453117, http://www.ppig.org/sites/default/files/2003-PPIG-15th-clarke.pdf

---

## Summary

**Total Criteria: 42**

- **Question 1 (C1-C15):** 15 criteria
  - Factory violations and coefficient: C1-C2
  - Factory time penalty extraction: C3-C5
  - Helper class speedup analysis: C6-C13
  - Coefficient comparison: C14-C15

- **Question 2 (C16-C26):** 11 criteria
  - Experience improvement: C16
  - Task speedups: C17-C21
  - Experience adjustment: C22-C23
  - Factory comparison: C24-C26

- **Question 3 (C27-C42):** 16 criteria (was 13 in TABLE_CRITERIA.md, expanded to 16 with proper structure)
  - Table structure: C27-C30
  - Column headers: C31-C33
  - Row 1 (Factory): C34-C36
  - Row 2 (Constructor Parameters): C37-C39
  - Row 3 (Helper Class): C40-C42

All criteria are independently verifiable with source citations from the five empirical papers.
