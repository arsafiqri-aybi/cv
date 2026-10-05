# Literature Discovery v0.1 — Breadth Pass

Date: 2026-10-06

## Method

This is a **breadth-first scientific map**, not a systematic review and not a claim of saturation.

The purpose is to identify the main research regions that materially affect CV construction and screening before forcing a module taxonomy.

Evidence emphasis:

1. meta-analyses / systematic reviews;
2. integrative reviews;
3. field / longitudinal studies;
4. controlled experiments;
5. technical audits / algorithmic studies;
6. transparent lower-tier evidence only for emerging gaps.

## Landscape

| Cluster | Current evidence density | Architecture role | Initial conclusion |
|---|---|---|---|
| Recruitment / staffing | strong | umbrella | CVs sit within a broader prehire system, not selection alone |
| Personnel selection | strong | umbrella + evaluation | validity, fairness, predictor/criterion distinctions are essential |
| Work / job analysis | strong | upstream role model | role relevance must be grounded in work requirements, not keyword counts |
| Résumé screening | moderate | direct domain | résumé content changes recruiter judgments, but validity remains contested |
| Signaling / information asymmetry | strong theory | mechanism | CV is a signal exchange under asymmetric information |
| Self-presentation / impression management | moderate | signal construction | presentation can change perceptions independently of underlying capability |
| Work experience | strong synthesis | evidence input | amount/duration alone weakly predicts performance |
| Biodata | strong synthesis | comparison construct | structured biodata can be predictive; ordinary CV ≠ biodata assessment |
| Skill signals | moderate experimental | signal content | some skill signals causally affect interview invitations |
| Education / credentials | moderate | signal content | education affects judgments, but meaning depends on role/context |
| Person–job fit | strong broader literature | human interpretation | perceived P–J fit matters, but is a judgment, not objective truth |
| Person–organization fit | strong broader literature | human interpretation | consequential but especially vulnerable to subjective interpretation |
| Recruiter inference | moderate | human interpretation | recruiters infer competence, fit, personality, etc.; accuracy varies |
| Recruiter attention | emerging/moderate | human interpretation | experience/education attention and review time relate to screening decisions |
| Writing quality | moderate, recent | document representation | clarity/detail/structure predict job-search success in at least one field context |
| Tailoring | emerging | document representation | associated with interview outcomes; independent effect requires more study |
| Layout / aesthetics | moderate, older | document representation | layout can influence shortlisting; formal layouts beat creative in one study |
| Personality inference from CV | moderate | non-edge / validity | paper/video resumes are poor tools for accurate personality inference |
| Digital selection | strong review | socio-technical context | selection technologies vary in validity and applicant reactions |
| ATS / parsing | emerging technical | machine interpretation | parsing is one technical function, not equivalent to ranking or selection |
| Algorithmic hiring | strong multidisciplinary survey | machine + fairness | systems, metrics, datasets and biases are heterogeneous |
| Hiring discrimination | strong meta-analysis | fairness | demographic cues can affect application outcomes; effects vary by group/context/time |
| Applicant reactions | strong review | broader system feedback | selection design can affect fairness perceptions and employer attraction |
| Generative AI + CV | emerging | signaling shift | AI can improve composition and destabilize what polished writing signals |
| AI resume screening bias | emerging | machine/fairness | LLM screening can reproduce gender-coded patterns; generalization is unresolved |
| Cross-cultural CV conventions | open | context | requires dedicated regional evidence before universal rules |
| Legal / policy constraints | context-specific | cross-cutting | must be jurisdiction-aware and kept separate from scientific laws |
| Application feedback | weak/noisy | feedback | interview/rejection outcomes are multi-causal and cannot identify mechanism alone |

## Anchor findings

### 1. Recruitment and selection are distinct but connected

Breaugh (2013) reviews recruitment as a domain involving recruitment targets, methods, messages, recruiters, job offers and applicant perspectives.

Potočnik et al. (2021) synthesize roughly 40 meta-analyses/reviews and organize recent developments around:
- selection;
- recruitment;
- technology.

Sackett, Lievens, & Landers (2026) review modern personnel selection through:
- predictor validity;
- new measurement approaches;
- fairness/bias;
- applicant reactions;
- AI.

**Architecture implication:** use Recruitment + Personnel Selection / Staffing as the broad scientific home.

### 2. Work reality precedes CV relevance

Sanchez & Levine (2012) distinguish major work-analysis information classes:
- work activities;
- worker attributes;
- work context.

**Architecture implication:** job descriptions are inputs to a target-role model, not the role model itself.

### 3. CV as signaling under information asymmetry

Bangerter, Roulin, & König (2012) model personnel selection as a signaling game in which applicants and organizations exchange information under partially conflicting incentives.

**Architecture implication:** signal construction deserves a mechanism layer, but persuasiveness must not be confused with evidentiary validity.

### 4. Resume information changes recruiter judgments

Cole et al. (2007) found recruiters' perceptions of recent-graduate employability were associated with combinations of academic qualifications, work experience, and extracurricular activities.

Tsai et al. (2011) found work experience and education affected hiring recommendations through recruiter-perceived person–job fit; work experience also affected P–O fit perceptions.

Chen et al. (2011) found recruiter inferences about professional knowledge, interpersonal skills, and general mental ability mediated relations between résumé information and hiring recommendations.

**Architecture implication:** human screening needs an inference layer, not a simple keyword-match model.

### 5. Screening influence does not establish performance validity

Zhang et al. (2025, conference proceedings abstract) directly challenge résumé criterion validity and report low point estimates across two samples.

Van Iddekinge et al. (2019) meta-analyzed 81 independent samples and reported corrected correlations of:
- .06 with job performance;
- .11 with training performance;
- .00 with turnover

for prehire work experience measures.

**Architecture implication:** callback effectiveness, screening judgment, and future performance validity must remain different outcome classes.

### 6. Structured biodata is not equivalent to ordinary CV review

A 2021/2022 meta-analysis of biodata examined 180 independent criterion-correlation samples and found substantially higher validity for some structured/scored biodata approaches.

**Architecture implication:** do not transfer biodata validity to free-form resumes.

### 7. Skill signals can causally affect interview invitations

Piopiunik et al. (2020) used randomized résumé signals with German HR managers and found cognitive and social skill signals affected interview invitation choices, with signal usefulness varying by applicant type/context.

**Architecture implication:** "what is on the CV" can have causal screening effects, but signal value is contextual.

### 8. Fit matters, but perceived fit is not ground truth

Kristof-Brown, Zimmerman, & Johnson (2005) meta-analyzed multiple forms of fit and found relationships with preentry and postentry criteria.

Tsai et al. (2011) show résumé information can influence hiring recommendations through perceived fit.

**Architecture implication:** distinguish:
- requirement match;
- evidence-supported relevance;
- perceived P–J fit;
- perceived P–O fit.

### 9. Composition quality has real screening consequences

Wingate et al. (2025) followed jobseekers in a Canadian co-op context.

Higher résumé writing quality was associated with a higher interview proportion; compositional factors improved prediction after controlling for program, experience, achievement and demographics.

The authors define writing quality around:
- detail;
- clarity;
- structure.

They also explicitly raise GenAI as a threat to interpreting polished writing as a stable applicant signal.

**Architecture implication:** writing quality is a document-transmission construct, not worker-performance evidence.

### 10. Layout matters, but not as a universal template law

Arnulf, Tegner, & Larssen (2010) experimentally varied résumé layout. Formal designs were preferred over more creative layouts in their setting.

**Architecture implication:** visual representation can affect screening. Do not promote one template as universally optimal.

### 11. Attention is measurable but context-specific

Pina et al. (2023) used eye tracking with recruiter résumé screening. Total viewing time and time spent on Experience and Education contributed to prediction of whether a résumé advanced.

**Architecture implication:** attention and scan behavior belong in human interpretation, but "7 seconds" folklore should not become a universal rule.

### 12. CV is poor personality measurement

Apers & Derous (2017), with real recruiters, found paper resumes generally did not support accurate Big Five inference; richer audio/video formats did not solve the validity problem.

**Architecture implication:** protect the non-edge:

```text
resume impression ≠ valid personality assessment
```

### 13. Impression management changes perceptions

Waung et al. (2017) found impression-management tactics in resumes/cover letters and experimentally showed some lower-intensity self-promotion / ingratiation tactics increased perceived fit.

**Architecture implication:** wording can alter impressions independent of objective qualifications; credibility calibration is necessary.

### 14. Machine mediation is heterogeneous

Woods et al. (2020) review digital selection procedures including:
- online applications;
- online tests;
- digital interviews;
- gamified assessment;
- social media.

Fabris et al. (2025) provide a multidisciplinary survey of algorithmic hiring systems, fairness measures, mitigation approaches, datasets, legal dimensions and socio-technical context.

**Architecture implication:** "ATS" must be decomposed into actual functions and assumptions.

### 15. Fairness is a system property, not a formatting check

Lippens et al. (2022/2023) synthesize 306 correspondence experiments from 169 studies, nearly 965,000 applications, across multiple discrimination grounds.

Schaerer et al. (2023) preregistered meta-analysis includes 244 effects from 85 field audits and 361,645 applications; gender-bias patterns changed over time and differed by job gender-typing.

**Architecture implication:** bias effects are real but context-sensitive; do not universalize direction or magnitude.

### 16. Digital systems also send signals to applicants

Folger et al. (2022) show digital selection methods can increase innovativeness perceptions while also decreasing procedural-justice perceptions in some contexts.

**Architecture implication:** hiring technology affects both organization→applicant and applicant→organization signaling.

### 17. Generative AI destabilizes traditional composition signals

Wingate et al. (2025) argue that if high-quality application writing is easier to produce with GenAI, its traditional signaling meaning may weaken or change.

Recent AI-screening research also indicates LLM-based screening can reproduce gender-coded patterns.

**Architecture implication:** GenAI is not merely a writing tool; it alters the economics and interpretation of signals.

## Research gaps promoted to explicit agenda

1. True criterion validity of holistic résumé review.
2. Incremental validity of résumé information beyond structured application forms/tests.
3. Role-specific importance of achievements vs responsibilities.
4. Validity of quantitative achievement claims as screening signals.
5. Generalizable effect of résumé tailoring independent of writing quality.
6. Modern recruiter behavior with AI-polished applications.
7. Actual production ATS behavior by system class.
8. Cross-cultural and jurisdiction-specific CV conventions.
9. Senior/executive vs early-career screening differences.
10. Creative-role vs technical-role layout effects.
11. How LLM screening interacts with résumé order, wording and demographic cues.
12. Whether AI-assisted résumé composition changes recruiter trust when disclosed or detected.
13. Reliability of recruiter judgments from résumé evidence.
14. How different evidence types should be calibrated by verifiability and diagnosticity.
15. How to learn from application outcomes without causal overreach.

## Breadth-pass conclusion

The initial process architecture survives the literature pass, but several refinements are now stronger:

```text
ROLE MODEL
↔ CANDIDATE REALITY
→ EVIDENCE UNITS
→ SIGNAL SELECTION
→ DOCUMENT ENCODING
→ HUMAN / MACHINE INFERENCE
→ SCREENING OUTCOME
```

The next scientific work is not to invent more stages. It is to decompose the constructs inside each stage while preserving cross-cutting validity, fairness, provenance and uncertainty.
