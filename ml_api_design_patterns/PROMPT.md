**Subdomain:** API Design Patterns

Your goal is to analyze empirical studies on API design pattern usability to synthesize findings across multiple papers and derive novel metrics through cross-study quantitative reasoning.

1. Quantify the cognitive usability cost of the factory pattern by determining how many dimensions from Clarke & Becker's framework are violated based on Ellis et al.'s empirical observations, then calculate a per-dimension time penalty coefficient. From Ellis, extract the factory pattern's time penalty ratio for the SSLSocket task, count total dimension violations, and divide the time penalty by violation count to derive a normalized per-dimension cost coefficient. Compare this to the helper class methods pattern by extracting speedup ratios across Stylos & Myers's three experimental tasks, calculating the average speedup, and computing its per-dimension coefficient using the same normalization approach. Calculate the ratio between the two coefficients to determine which API design pattern imposes greater cognitive cost per violated dimension.

2. Synthesize findings across studies to derive an experience-adjusted API pattern complexity metric by extracting the percentage improvement in task completion time for experienced versus less experienced developers on complex tasks from Piccioni et al., calculating the average speedup ratio between starting class methods and helper class methods across Stylos & Myers's three experimental tasks, and applying Piccioni's experience benefit percentage to adjust this average speedup to derive an Experience-Adjusted Method Placement Penalty. Compare this experience-adjusted penalty to Ellis's factory pattern time penalty ratio for the SSLSocket task and calculate the ratio to determine which API design approach imposes greater cognitive cost even after accounting for developer experience.

3. Create an image of a table comparing API design patterns across the empirical studies with exactly 3 data rows (excluding header) and exactly 3 columns. The table must have the exact title: "API Design Pattern Usability: Empirical Evidence Synthesis". Column headers must be: "Pattern", "Time Penalty (vs. Baseline)", "Cognitive Violations". Row 1 must be labeled "Factory Pattern" and contain Ellis's SSLSocket data (time penalty as ratio, number of Clarke dimensions violated). Row 2 must be labeled "Required Constructor Parameters" and contain Stylos & Clarke's data (comparing to create-set-call baseline, number of violated dimensions). Row 3 must be labeled "Helper Class Methods" and contain Stylos & Myers's Email task data (time penalty ratio, number of violated dimensions).

## Citations

[1] Ellis, B., Stylos, J., & Myers, B. (2007). The factory pattern in API design: A usability evaluation. In *29th International Conference on Software Engineering (ICSE'07)* (pp. 302-312). IEEE. http://www.cs.cmu.edu/~NatProg/papers/Ellis2007FactoryUsability.pdf

[2] Stylos, J., & Clarke, S. (2007). Usability implications of requiring parameters in objects' constructors. In *29th International Conference on Software Engineering (ICSE'07)* (pp. 529-539). IEEE. http://www.cs.cmu.edu/afs/cs/Web/People/marmalade/papers/Stylos2007CreateSetCall.pdf

[3] Piccioni, M., Furia, C. A., & Meyer, B. (2013). An empirical study of API usability. In *2013 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement* (pp. 5-14). IEEE. https://se.inf.ethz.ch/~meyer/publications/empirical/API_usability.pdf

[4] Clarke, S., & Becker, C. (2003). Using the Cognitive Dimensions Framework to evaluate the usability of a class library. In M. Petre & D. Budgen (Eds.), *Proc. Joint Conf. EASE & PPIG 2003* (pp. 359-366). http://www.ppig.org/sites/default/files/2003-PPIG-15th-clarke.pdf

[5] Stylos, J., & Myers, B. A. (2008). The implications of method placement on API learnability. In *Proceedings of the 16th ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE'08)* (pp. 105-112). ACM. https://doi.org/10.1145/1453101.1453117
