# SOURCE SUMMARY: Stylos & Clarke (2007) - Constructor Parameters Usability

**Full Citation:** Stylos, J., & Clarke, S. (2007). Usability implications of requiring parameters in objects' constructors. In 29th International Conference on Software Engineering (ICSE'07) (pp. 529-539). IEEE.

---

## STUDY OVERVIEW

**Research Question:** How do required constructor parameters compare to create-set-call (parameterless default constructors) in API usability across different programmer personas?

**Main Finding:** Contrary to expectations, programmers strongly preferred and were more effective with create-set-call APIs (default constructors + property setters) rather than required constructor parameters.

**Hypothesis (NOT supported):** Required parameters would create more usable and self-documenting APIs by guiding programmers and preventing errors.

**Actual Result:** Create-set-call pattern was preferred and more effective for ALL three programmer personas.

**Participants:** 30 professional programmers from three distinct personas
- 10 Systematic programmers (C++, 5+ years experience)
- 10 Pragmatic programmers (C#, 2+ years experience)
- 10 Opportunistic programmers (Visual Basic, 2+ years experience)

**Methodology:** Six programming tasks (create, debug, read code) using think-aloud protocol

**Study Duration:** 2 hours 15 minutes per participant

---

## THREE PROGRAMMER PERSONAS

### Systematic Programmers
**Work Style:** Top-down, defensive programming
- Understand system as whole before focusing on components
- Mistrust API guarantees, prefer additional testing
- Want to understand WHY code works, not just that it works
- Rare persona, prefer C++, C, assembly

**Recruitment Criteria:**
- 5+ years professional experience
- C or C++ primary language
- Large projects with reliability emphasis

**Constructor Preference:** Create-set-call
**Reasoning:**
- Greater flexibility in initialization order
- Can use return codes instead of exceptions for each property
- More granular control

**Effectiveness:** Equally effective with both patterns, but preferred create-set-call

### Pragmatic Programmers
**Work Style:** Bottom-up with top-down fallback
- Learn as they go, starting with specific task
- Willing to trade control for simplicity
- Want awareness and control of tradeoffs
- Use tools like GUI editors but want to edit generated code
- Prefer Java, C#

**Recruitment Criteria:**
- 2+ years professional experience
- C# primary language
- Desktop applications using WinForms

**Constructor Preference:** Create-set-call
**Reasoning:**
- Initialization flexibility (create in one place, initialize elsewhere)
- Less restrictive
- Minor stumbling block with required constructors

**Effectiveness:** More effective than opportunistic with required constructors, but still more effective with create-set-call

### Opportunistic Programmers
**Work Style:** Bottom-up, task-focused
- Don't want to worry about low-level details
- Get code working as quickly as possible
- Most common persona
- Prefer Visual Basic, high productivity languages

**Recruitment Criteria:**
- 2+ years professional experience
- Visual Basic primary language
- Preferred: no formal computer degree
- Web applications using HTML and Visual Basic

**Constructor Preference:** Create-set-call
**Reasoning:**
- Required constructors unfamiliar and unexpected
- Even after repeated exposure, continued to have difficulty

**Effectiveness:** Benefited most from create-set-call; had persistent difficulties with required constructors

---

## KEY QUANTITATIVE RESULTS

### Task 1: Notepad Programming (Expectation Task)
**Result:** 30/30 participants (100%) used create-set-call in their imagined code
- **Factory usage:** 0/30 considered using factories
- **Subclass creation:** 3/30 created separate subclasses
- No participant used or considered required constructors

### Task 1-B: File API Design (Systematic Only)
**Result:** 10/10 systematic programmers (100%) designed APIs with default constructors
- Surprising: All had experience with Microsoft file APIs which DON'T provide default constructors
- Most also provided optional constructor accepting filename parameter

### Task 2: Files and Emails (Between-Subjects)
**Condition A:** Default constructors (create-set-call)
**Condition B:** Required constructors
**Result:** Create-set-call condition completed with less difficulty than required-constructor condition

### Task 3: Domain-Independent Classes (Within-Subjects)
**Two objects:** One with required constructor, one with create-set-call

**Opportunistic & Pragmatic Behaviors:**
- Multiple participants attempted to pass `null` to required constructor (caused runtime exception)
- No participant tried setting property to `null` for create-set-call

**Discovery Speed:**
- **Create-set-call:** Participants quickly discovered which 3 of 9 properties were necessary
- **Required constructor:** Many vocalized wrong assumptions, slow to discover actual problem
- Participants often assumed compiler errors were syntactic, not semantic

**Comfort Levels:**
- Opportunistic: Less hesitant to start (more comfortable than Notepad task)
- Pragmatic: Less comfortable starting without understanding domain/goal

### Task 4: Message Queue Debugging (Between-Subjects)
**Bug:** `DenySharedReceive` property set to `true`, causing runtime exception

**Condition A:** Default constructor + property setter (`messageQueue.DenySharedReceive = true;`)
**Condition B:** Four-parameter constructor (2nd parameter = DenySharedReceive)

**Result:**
- Few participants in create-set-call condition had difficulties with Boolean constructor arguments
- Difficulties neither common nor severe
- IDE features helped overcome readability differences
- No significant difference in debugging effectiveness

### Task 5: Optional Constructors (Single Condition)
**Design:** 5 objects with varying complexity, each providing both default constructor AND convenience constructors

**Results:**
- Most participants used create-set-call even when convenience constructors available
- Participants tended to use EITHER create-set-call OR convenience constructors for ALL objects (not mixing)
- Starting with complex vs simple objects did NOT influence constructor choice
- **Key Finding:** Optional constructors (when default also provided) caused NO negative impact
- Sometimes helpful to pragmatic programmers (suggested property combinations, shorter syntax)

### Task 6: Reading Code on Paper (Between-Subjects)
**Condition A:** Constructor with Boolean parameters (`new Foo(true, true)`)
**Condition B:** Create-set-call with Boolean properties (`obj.sharing = true; obj.caching = true;`)

**Result:**
- Constructor calls conveyed less information (no parameter names visible)
- Participants did NOT skim over parameters as hypothesized
- Participants were aware of their lack of knowledge
- **Important:** None of participants read paper code as part of professional job

### Interview Results
**Preference:** Nearly all participants (≈27/30) preferred create-set-call

**Justifications for Create-Set-Call:**

1. **Initialization Flexibility** (Common with Pragmatic)
   - Create object in one place, initialize elsewhere
   - Possibly in another class or package

2. **Less Restrictive**
   - APIs should let consumers decide how to do things
   - Don't force one way over another

3. **Consistency** (From 2 API creators)
   - Most APIs have default constructors
   - People expect them

4. **More Control** (Systematic programmers)
   - Set each property individually
   - Deal with errors using return codes (not just exceptions)

---

## COMMON BEHAVIORAL PATTERNS

### Assumption of Default Constructors
**Finding:** Opportunistic and pragmatic programmers consistently assumed default constructor exists for ANY class

**Evidence:**
- Wrote code calling default constructor
- Didn't notice compilation error until 1-2 lines later
- Misunderstood WHY constructor wouldn't compile

**Interpretation of Compiler Errors:**
- Opportunistic programmers assumed SYNTACTIC error (missing parenthesis, keyword)
- NOT semantic error (missing required parameters)
- Caused participants to doubt their own syntax knowledge
- Same participants rarely made syntax errors with create-set-call APIs

**Persistence:** Assumptions did NOT change over course of study, even after exposure to multiple required-constructor APIs

### Required Constructors as Syntactic Barriers
**Finding:** Participants interpreted required constructors as syntactic barriers to compilation, not functional requirements

**Common Workarounds (Both Failed):**
1. **Pass `null` for parameters** → Runtime exception in study APIs
2. **Create empty new objects for each parameter** → Objects uninitialized/invalid

**Quote Examples:**
- "I don't like doing this. It probably won't work." (about passing null)

### IDE Features in Debugging
**Finding:** IDE features (code-completion) negated readability differences between patterns when debugging

**Behavior:**
- All participants used code-completion to access constructor parameter information
- Even ambiguous code like `new Foo(true, true)` not significantly harder to debug than `obj.sharing = true; obj.caching = true;`

### Optional Constructors Have No Negative Impact
**Finding:** Constructors provided IN ADDITION to default constructor were sometimes helpful, never harmful

**Benefits:**
- Suggested property combinations that work together
- Provided shorter mechanism for initializing multiple properties
- Most helpful to pragmatic programmers

---

## COGNITIVE DIMENSIONS ANALYSIS

### Premature Commitment
**Definition:** Having to make decisions before having necessary information

**Required Constructors Create Premature Commitment:**
- Programmers must decide constructor parameters BEFORE exploring object's properties/methods
- Interrupts natural exploration workflow

### Work-Step Unit
**Definition:** How much work must be done in a single unit

**Required Constructors Increase Work-Step Unit:**
- Must satisfy constructor before exploring if object is correct one
- Often requires recursively instantiating objects for each parameter
- Create-set-call allows incremental, interruptible exploration

### Diffuseness
**Definition:** How much space/verbosity code requires

**Required Constructors Decrease Diffuseness:**
- More compact code
- But NO observed increase in readability as result

---

## PROGRAMMER STRATEGY MODEL

**Figure 2 Workflow Model:**

```
1. What Object Do I Use?
   ↓
2. Instantiate the object
   ↓
[REQUIRED CONSTRUCTOR PATH]
→ Satisfy Required Constructor (INTERRUPTION)
   ↓
[BACK TO MAIN PATH]
3. Is This the Right Object? | What Properties or Methods Do I Need?
   ↓
4. Call the method / Set the property
   ↓
5. Do I Have to Do Anything Else? | What's the Next Step?
   ↓
[Loop back to step 3]
```

**Key Insight:** Required constructors interrupt exploration between steps 2 and 3, forcing premature commitment

**With Create-Set-Call:**
- Exploration of instance properties/methods directly follows finding candidate object
- Natural, uninterrupted workflow

**With Required Constructors:**
- Must satisfy constructor before exploring object
- Often by recursively instantiating required parameter objects
- Cannot determine if object is correct one until after satisfying constructor
- Participants "wanted current construction problem to go away" so they could continue finding right object

---

## STUDY DESIGN DETAILS

### Task Descriptions

**Task 1: Notepad Programming**
- Write code to read file and send contents in email body
- Use only Notepad text editor
- No code checking/compilation
- **Purpose:** Elicit expectations without influence of code-completion, examples, docs
- **Condition:** Single (no provided code)

**Task 1-B: File API Design (Systematic Only)**
- Design API for file reading/writing operations
- Write declarations without implementing
- Use Notepad
- **Purpose:** Elicit assumptions from experienced API designers
- **Condition:** Single (replaced Task 1 for systematic programmers)

**Task 2: Files and Emails**
- Same task as Task 1, but in Visual Studio with real APIs
- Template project linked to one of two libraries
- **Library A:** Default constructors only
- **Library B:** Required constructors only
- **Purpose:** Between-subjects comparison of effectiveness
- **Conditions:** Two (create-set-call vs required constructors)

**Task 3: Domain-Independent Classes**
- Create and use two objects: "CptrObject" and "CptrModel"
- Call `use()` method on each
- Made-up domain (plausible but incomprehensible names)
- **One object:** Required constructor
- **Other object:** Default constructor + required properties
- Create-set-call object threw runtime exception if properties not set
- **Purpose:** Test how patterns convey requirements in unfamiliar domain
- **Conditions:** Single (within-subjects, each participant created both)

**Task 4: Message Queue Debugging**
- Debug 100-line program using .NET System.Messaging API
- Bug: `DenySharedReceive` set to `true` (should be `false`)
- Must fix in two locations
- **Condition A:** Default constructor + property setter
- **Condition B:** Four-parameter constructor (2nd param = DenySharedReceive)
- **Purpose:** Compare readability and debugability
- **Conditions:** Two (between-subjects)

**Task 5: Optional Constructors**
- Initialize online store inventory
- 5 objects with up to 5 properties each
- Each object provided: default constructor AND convenience constructors
- Example: Book (author, title, ISBN) vs Magazine (title, ISBN)
- **Condition A:** Objects presented in increasing complexity
- **Condition B:** Objects presented in decreasing complexity
- **Purpose:** Test usability of optional "convenience" constructors
- **Conditions:** Two (presentation order)

**Task 6: Reading Code on Paper**
- Paper printout of short program (≈12 lines)
- Explain what program does
- Imaginary APIs with Boolean parameters
- **Condition A:** Boolean constructor arguments
- **Condition B:** Create-set-call with Boolean properties
- **Purpose:** Test readability without IDE features
- **Conditions:** Two (between-subjects)

### Study Environment
- **Location:** Usability lab, one-way mirror separation
- **Computer:** PC with Visual Studio 2005, screen capturing
- **Internet Access:** Yes
- **Language by Persona:**
  - Systematic → C++
  - Pragmatic → C#
  - Opportunistic → VB.NET
- **API Sharing:** Cross-language .NET assemblies (same APIs across languages)

### Interview Protocol
- **Timing:** After programming tasks
- **Format:** Semi-structured, face-to-face
- **Revelation:** Focus of study revealed after tasks
- **Topics:**
  - Participant opinions on constructor patterns
  - APIs used in professional work
  - API design practices if applicable

---

## STUDY LIMITATIONS

### Causal Claims
- Results are hypotheses backed by systematic observation
- Not making causal claims from research perspective

### Ordering Effects
- Tasks performed in same order for all participants
- Intentional: guaranteed exposure to both patterns before debugging/optional constructor tasks
- Mitigated: Expectations didn't change even after exposure to required constructors

### Task Length and Familiarity
- Individual tasks relatively small
- Participants unfamiliar with APIs before study
- May not generalize to long-term use of familiar APIs
- Would require longer studies (multiple sessions) or field studies

### Language Generalization
- Consistency across C++, C#, VB.NET suggests generalization to other OO languages
- But differing syntax (e.g., Objective-C named parameters) may offer different results

### Participant Representativeness
- Professional programmers representative of .NET framework users
- Even experienced professionals had difficulties
- Less experienced developers likely to have AT LEAST as much difficulty

### Task Representativeness
- Tasks smaller than typical programming tasks
- BUT object construction typically occurs at beginning of tasks
- Constructor/parameter setting in study tasks likely representative of larger tasks

---

## IMPORTANT PAGE/SECTION REFERENCES

**For Verification:**

- **Abstract (p.1):** Main findings - contrary to expectations, create-set-call preferred and more effective
- **Figure 1 (p.1):** Visual comparison of create-set-call vs required constructor patterns
- **Section 3.1 (p.3):** Persona descriptions and recruitment criteria
- **Section 4.1 (p.6):** Common participant behavior across personas
- **Section 4.2 (p.7):** Task 1 results - 30/30 used create-set-call
- **Section 4.3 (p.7):** Task 1-B results - 10/10 systematic designed with default constructors
- **Section 4.9 (p.7):** Interview results - nearly all preferred create-set-call
- **Section 5 (p.8):** Discussion of findings by persona
- **Section 6 (p.8):** Model of programmers' strategies (Figure 2)
- **Figure 2 (p.8):** Workflow diagram showing required constructor interruption

---

## CROSS-STUDY SYNTHESIS NOTES

**Comparison Points with Other Studies:**
- Total participants: 30 (10 per persona)
- Programming experience: 2-5+ years depending on persona
- Study type: Mixed methods (qualitative + observational)
- Primary statistical approach: Qualitative analysis, systematic observation
- No p-values reported (not hypothesis-testing study design)

**Key Metrics for Synthesis:**
- Constructor expectation: 100% (30/30) expected/preferred create-set-call
- Systematic API design: 100% (10/10) designed with default constructors
- Optional constructors: No negative impact found
- Persona distribution: Equal (10 systematic, 10 pragmatic, 10 opportunistic)

---

## THEORETICAL CONTRIBUTIONS

### Cognitive Dimensions Framework Application
- **Premature Commitment:** Required constructors force decisions before exploration
- **Work-Step Unit:** Required constructors increase unit size
- **Diffuseness:** Required constructors more compact but not more readable

### Programmer Behavior Model
- Systematic workflow model for object exploration
- Identified key interruption point where required constructors interfere
- Explains WHY create-set-call is more effective

### Persona-Based Design
- Different personas have different reasons for same preference
- Even personas expected to benefit from required constructors preferred create-set-call
- Validates persona-based API design approach

---

## PRACTICAL RECOMMENDATIONS

### Primary Recommendation
**Avoid required constructor parameters in new APIs, favor create-set-call pattern**
- **Especially for:** APIs targeting opportunistic programmers

### Optional Constructors
**Provide optional convenience constructors IN ADDITION to default constructor**
- No negative impact
- Sometimes helpful (especially to pragmatic programmers)
- Suggests property combinations
- Provides shorter syntax option

### When to Use Create-Set-Call
- **All personas preferred it**
- **Opportunistic:** Critical for effectiveness
- **Pragmatic:** Minor but important usability improvement
- **Systematic:** Flexibility and granular control

### When Required Constructors Might Be Acceptable
- **Study suggests:** Very limited cases
- **Not recommended:** Even for systematic programmers who handled them well but still preferred create-set-call

---

## FUTURE RESEARCH DIRECTIONS

### 1. Runtime Exceptions vs Compiler Errors
**Surprising Finding:** Runtime exceptions more effective than compiler errors at conveying requirements

**Research Question:** How do different error types interact with programmer work styles?

**Potential Approach:**
- IDE "exploration mode" that doesn't show certain errors until "spot check"
- Broader comparison of compiler errors vs runtime exceptions

### 2. Object Decomposition
**Finding:** Programmers slow to change assumptions about what classes should exist

**Research Question:** How do programmers make class existence assumptions?

**Topics:**
- Single Mail class vs MailMessage + MailServer
- How APIs can service multiple assumption sets
- How tools can increase awareness of assumptions

### 3. Debugging Strategies by Persona
**Finding:** Different personas have markedly different debugging effectiveness

**Strategies:**
- **Systematic:** Top-down (understand system as whole first)
- **Opportunistic:** Bottom-up (start from error line), struggled with multi-component bugs
- **Pragmatic:** Bottom-up with top-down fallback

**Research Question:** What types of bugs are most problematic for each persona?

**Application:** API designers can avoid difficult errors for target audience

---

## RELATIONSHIP TO FACTORY PATTERN STUDY

**Same Authors:** Stylos co-author on both Ellis et al. (2007) and this study
**Same Institution:** Carnegie Mellon University + Microsoft collaboration
**Complementary Findings:**
- **Ellis et al.:** Factories harder than constructors
- **Stylos & Clarke:** Required constructors harder than create-set-call
- **Combined Message:** Simple constructors (no required params) most usable

**Study Design Similarities:**
- Think-aloud protocol
- Mixed task types (creation, debugging, reading)
- Professional programmer participants
- Focus on common API design choices

**Key Difference:**
- **Ellis et al.:** Quantitative with statistical significance testing
- **Stylos & Clarke:** Qualitative with systematic observation
- **Ellis et al.:** 12 participants, single persona variable
- **Stylos & Clarke:** 30 participants, three distinct personas
