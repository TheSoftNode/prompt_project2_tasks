# SOURCE SUMMARY: Ellis et al. (2007) - Factory Pattern Usability

**Full Citation:** Ellis, B., Stylos, J., & Myers, B. (2007). The factory pattern in API design: A usability evaluation. In 29th International Conference on Software Engineering (ICSE'07) (pp. 302-312). IEEE.

---

## STUDY OVERVIEW

**Research Question:** How does the factory pattern compare to constructors in API usability?

**Main Finding:** Factories are significantly more time-consuming and difficult for programmers to use than constructors, regardless of context or programmer experience level.

**Participants:** 12 programmers with 1-22 years of Java experience
- 8 had professional programming experience
- 8 were computer science students
- 6 had some experience with factory pattern
- 4 had considerable factory pattern experience

**Methodology:** Five Java programming tasks using think-aloud protocol

---

## KEY QUANTITATIVE RESULTS

### Task 1: Thingies Task (Context-Neutral)
- **Squark (Factory):** Median time = 7:10 (430 seconds), SD = 3:53
- **Flarn (Constructor):** Median time = 1:20 (80 seconds), SD = 0:50
- **Statistical Significance:** p = 0.005 (highly significant)
- **Time Distribution:** Participants spent 84.3% of time on factory vs 15.7% on constructor
- **Completion Rate:** 10/12 participants (2 ran out of time)

### Task 2: Sockets Task (Real-World API)
- **SSLSocket (Factory):** Mean time = 20:05 (1205 seconds), SD = 11:17, Median = 16:05
- **MulticastSocket (Constructor):** Mean time = 9:31 (571 seconds), SD = 8:04, Median = 7:41
- **Statistical Significance:** p = 0.005 (highly significant)
- **Failure Rate:** 5/12 participants (41.7%) failed to complete SSLSocket task
- **Success Rate:** All participants who reached MulticastSocket completed it

### Task 3: PIUtils Task (Debugging)
- **Factory Condition:** Mean = 17:00, SD = 10:26 (n=6)
- **Constructor Condition:** Mean = 26:40, SD = 2:26 (n=3)
- **Statistical Significance:** p = 0.169 (not significant, but high variance)
- **Completion:** 9/12 participants (3 ran out of time)

### Task 4: Notepad Email (Expectation)
- **Result:** 12/12 participants (100%) used constructors in their implementation
- **Factory Usage:** 0/12 participants considered using a factory
- **Subclass Creation:** 3/12 created separate email subclasses

### Task 5: Eclipse Email (Discovery)
- **Attempted Constructor First:** 7/10 participants (70%)
- **Attempted Subclassing:** 3/10 participants
- **Eventually Used Factory:** 10/10 participants (100% completion)

---

## QUALITATIVE FINDINGS

### Usability Problems with Factories

**Problem 1: Finding the Factory**
- All participants expected constructors to exist
- Confusing error message: "Cannot instantiate the type SSLSocket" (misleading - suggests import/syntax error)
- 6/12 participants (50%) believed they needed to create subclasses
- Documentation phrase "Used only by subclasses" universally misunderstood

**Problem 2: Abstract Factory Complexity**
- Factory itself is abstract class, requiring factory method to obtain instance
- Participants struggled with: "Why is it an abstract class? SSLSocket is an abstract class too."
- Static `getDefault()` method not immediately discoverable

**Problem 3: Return Type Covariance Issues**
- Overridden methods cannot change return type
- `SSLSocketFactory.getDefault()` returns `SocketFactory` (superclass type)
- Participants uncertain if returned object was actually SSLSocketFactory
- Comment: "So it seems like I can't instantiate an SSLSocket. And it won't tell me who can."

**Problem 4: Method Inheritance Confusion**
- `createSocket()` methods inherited from superclass
- Documentation only listed method names, not signatures
- One participant: "Methods inherited from SocketFactory: createSocket, createSocket, createSocket, createSocket, createSocket. Sigh."

**Problem 5: Explicit Downcasting Required**
- `createSocket()` returns generic `Socket` objects (polymorphically typed)
- Participants needed SSLSocket-specific methods
- Required explicit downcast from Socket to SSLSocket
- Eroded confidence: "I don't like doing this. It probably won't work."
- Strong objection: "You should never have to typecast. If you write programs that require you to typecast, you've either done something wrong or you need to support covariant typing."

**Problem 6: Documentation Placement**
- Critical information buried at bottom of long class descriptions
- Participants scrolled past quickly, never reading key sentences
- Most found factory only by lexical proximity in class list
- Only 3/12 participants actually read the relevant documentation

**Problem 7: Treating Factories as Constructors**
- 5/12 participants called factory methods and ignored return value
- One participant called factory method then typecast the factory to product type
- Misconception that factory method transforms the factory into product

### Constructor Advantages

**Simplicity:** Most common comment about constructors: "oh, that should be easy"

**Natural Expectation:** Constructors match programmer mental model of object creation

**Relief Upon Discovery:** "oh good, I can just create one" (implying factories are more complex)

**No Problems:** Zero participants had difficulties with constructor-based tasks

---

## PARTICIPANT QUOTES

### On Factory Complexity
- "I'm trying to figure out how to use these factories. It seems like there's a whole lot of abstract stuff floating around, and I'm not going to be able to actually instantiate anything that I need. In fact, I forgot how I even got here."

### On Documentation
- "'Used only by subclasses' makes you want to instantiate subclasses. That's really really confusing."
- "'Public abstract class'. It extends SocketFactory. It's an abstract class. SSLSocket is an abstract class too. Why is it an abstract class?"

### On Downcasting
- "You should never have to typecast. If you write programs that require you to typecast, you've either done something wrong or you need to support covariant typing."
- "It's counterintuitive where you have to downcast to something. It's really bad. You should write to the Java people; you should say in your paper, 'get rid of it.'"

### On Constructor Simplicity
- "oh good, I can just create one" (when finding MulticastSocket has constructors)

---

## FACTORY PATTERN ALTERNATIVES

### Class Clusters (Recommended Alternative)

**Definition:** Pattern from Smalltalk/Objective-C where parent class depends on children, but no separate factory class needed. The "factory" IS the "product."

**Advantages over Factory:**
1. **Simpler Interface:** Appears as single concrete class with constructor
2. **No Parallel Hierarchies:** Only one class hierarchy instead of two (products + factories)
3. **No Downcasting:** Constructor can return correctly typed object
4. **Locality:** All logic in one class rather than factory + product

**Implementation in Java (using handle-body idiom):**

```java
public class Widget {
    private Widget body;

    public Widget(boolean condition) {
        if (condition) {
            body = new WidgetA();
        } else {
            body = new WidgetB();
        }
    }

    public void performAction() {
        body.performAction();
    }
}

class WidgetA extends Widget { ... }
class WidgetB extends Widget { ... }
```

**Usage:** `Widget w = new Widget(true);` // Gets WidgetA implementation

**Can Achieve Same Benefits as Factory:**
- Hide private subclass implementations
- Avoid allocating new objects each time (e.g., socket pools)
- Perform environment-specific checks in constructor
- Dynamic behavior selection

---

## FACTORY PATTERN IN THE WILD

### Java API (1.5 SE)
- **61 factory classes/interfaces** (out of 3,279 total classes)
- Strong mapping between product and factory class names
- Used for: sockets, preferences, threads, UI controls, database connectors, security

### .NET API
- **13 factory classes** (out of 2,686 total classes)
- Often come in pairs (ISecureFactory + SecureFactory)
- More monolithic approach - one factory returns wide range of objects
- Used for: database connectors, configuration, settings, security

### Common Use Cases
- Shared resources and OS-managed objects
- Sockets, preferences objects, threads
- User interface controls
- Security measures

---

## THEORETICAL BACKGROUND

### Benefits of Factory Pattern (from Gang of Four)

1. **Dependency Inversion:** Client depends only on abstracts, never concrete subclasses
2. **Decoupling:** Factories can be swapped without touching client code
3. **Consistent Products:** All instantiated using same factory
4. **Encapsulation:** Hides concrete implementations

### Liabilities of Factory Pattern

**From Gang of Four:**
- Difficulty adding new product types (need new factory classes/methods)

**From This Study:**
- **Instantiation Complexity:** Requires factory method in abstract factory to avoid client knowing concrete factory class
- **Explicit Downcasting:** True abstract factories require downcasting product instances
- **Increased Code Complexity:** Two parallel hierarchies instead of one
- **Discoverability:** Hard to find entry point when constructors are protected/private

---

## DEBRIEFING SURVEY RESULTS

**Presented Two Code Samples:** BorderFactory vs direct Border construction

**Preferences:**
- **6/12 favored factories**
- **5/12 favored constructors**
- **1/12 unclear**

**Reasons for Preferring Factories (despite struggling with them):**

**Category 1: Hiding Complexity (2 participants)**
- Factories hide complexity behind simple interface
- "Opaque" objects should use factories
- Objects whose functionality code depends on should use constructors

**Category 2: Deference to API Designers (4 participants)**
- API designers must be more knowledgeable
- Factories appear more difficult due to personal failure to understand
- "I think that [constructor] is easier to understand, and therefore I like it better. However [factory] is probably better since it uses a factory and it appears that factories are probably useful in some way."
- "I like [factory] better. I can't quite recall all the benefits of using [the] factory pattern, but I guess from all the training and previous programming experiences I just feel safer and more in control using factories." (from participant who struggled extensively)

**Key HCI Insight:** Users cannot always identify best solution when presented explicit choice. Perceived complexity may be interpreted as evidence of advanced design.

---

## STUDY DESIGN DETAILS

### Task Descriptions

**1. Notepad Email Task**
- First task, plain-text editor
- Write code to construct email object with sender, recipient, body, type (plain/rich)
- Elicit programmer expectations about object creation
- No factory provided

**2. Eclipse Email Task**
- Same task description as Notepad
- Pre-built email API using factory pattern
- Measure reaction to finding factory when constructor expected

**3. Thingies Task**
- Context-neutral task (no domain knowledge)
- Create "Squark" (factory-based) and "Flarn" (constructor-based)
- Call run() method on each
- Within-subjects comparison

**4. PIUtils Task**
- Debugging task with pre-written code
- Find and fix bug in dialog layout code
- Two conditions: factory vs class cluster (between-subjects)

**5. Sockets Task**
- Real-world Java API usage
- Construct SSLSocket (factory) and MulticastSocket (constructor)
- Configure both to connect to server and port

### Measurement Approach
- **Primary Metric:** Time to completion
- **Think-Aloud Protocol:** Participants verbalized goals, assumptions, strategies
- **Task Order:** Randomized to minimize learning effects
- **Documentation:** Full access to Java 1.5 SE API documentation

---

## STATISTICAL ANALYSIS

### Normality Testing
- Thingies data tested for normality
- Not significantly non-normal (p=0.274 Squark, p=0.129 Flarn)
- Sufficiently skewed to warrant non-parametric tests

### Tests Used
- **Wilcoxon Signed Ranks Test:** For within-subjects comparisons (Thingies, Sockets)
- **One-way ANOVA:** For between-subjects comparison (PIUtils)

### Effect Sizes
- Thingies: Z = -2.81, p = 0.005 (highly significant)
- Sockets: Z = -2.803, p = 0.005 (highly significant)
- PIUtils: F = 2.35, p = 0.169 (not significant, high variance)

---

## CONCLUSIONS AND RECOMMENDATIONS

### Primary Findings
1. Factories significantly more time-consuming than constructors (p=0.005)
2. High failure rate for factory tasks (41.7% for SSLSocket)
3. 100% of participants naturally expected and preferred constructors
4. Results consistent across context-free and real-world tasks
5. Experience level did not mitigate factory difficulties

### Recommendations
1. **Avoid factories where alternatives exist** (constructors, class clusters)
2. **Use class clusters** when need to hide subclass implementations
3. **Improve documentation** if factories unavoidable:
   - Place critical information at top of class descriptions
   - Clarify entry points explicitly
   - Avoid misleading phrases like "Used only by subclasses"
4. **Improve error messages** for protected constructors
5. **Consider language support** for factories if pattern must be used

### Future Work Suggestions
- Compare class clusters vs factories from API developer perspective
- Study factory pattern in debugging contexts with larger samples
- Examine other design patterns (singleton, observer, command)
- Study API metaphors (event handlers, threading models)
- Reconcile user expectations with cognitive dimensions framework

---

## IMPORTANT PAGE/SECTION REFERENCES

**For Verification:**

- **Abstract (p.1):** Main findings summary, p=0.005 significance
- **Section 4.1 (p.4):** Participant demographics (n=12, 1-22 years experience)
- **Section 5.1 (p.5-6):** Notepad Email results (12/12 used constructors)
- **Section 5.3 (p.6):** Thingies results (7:10 vs 1:20, p=0.005)
- **Section 5.5 (p.6-7):** Sockets results (20:05 vs 9:31, 5/12 failed factory task)
- **Figure 2 (p.6):** Box plot showing time distributions
- **Section 6.1 (p.7-8):** Qualitative findings on discovering factories
- **Section 6.2 (p.8-9):** Qualitative findings on using factories
- **Section 6.3 (p.9):** Debriefing survey (6/12 preferred factories despite struggling)

---

## CROSS-STUDY SYNTHESIS NOTES

**Comparison Points with Other Studies:**
- Total participants: 12
- Programming experience range: 1-22 years
- Median experience: ~5 years (estimated from range)
- Statistical measure: Wilcoxon Signed Ranks Test, p-values
- Highly significant results: 2 tasks (Thingies, Sockets) both p=0.005

**Key Metrics for Synthesis:**
- Factory completion time: Mean ~20 minutes, high variance
- Constructor completion time: Mean ~5-10 minutes, low variance
- Factory failure rate: 41.7% (5/12 participants)
- Constructor failure rate: 0% (0/12 participants)
