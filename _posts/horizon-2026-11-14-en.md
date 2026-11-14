# Horizon Daily - 2026-11-14

> From 126 items, 16 important content pieces were selected

---

1. [Lovable-built apps leak passports and 200K+ private messages via insecure Supabase defaults](#item-1) ⭐️ 8.0/10
2. [SpaceX catches Super Heavy booster to close Starship Flight 15](#item-2) ⭐️ 8.0/10
3. [Report: Nvidia CEO Jensen Huang Resigns; Trump Won't Raise Issue in China](#item-3) ⭐️ 8.0/10
4. [Show HN: DeepSeek V3's core ideas rebuilt from scratch in ~200 lines of pure JAX](#item-4) ⭐️ 7.0/10
5. [Google Project Zero moves to 90-day disclosure, with 60 and 30 days coming](#item-5) ⭐️ 7.0/10
6. [EFF: Tech Companies Are Trying to Redefine Privacy Again](#item-6) ⭐️ 7.0/10
7. [Blog Maps the Family Tree of Software Job Titles](#item-7) ⭐️ 6.0/10
8. [PyPI rolls out redesigned project pages highlighting provenance and security signals](#item-8) ⭐️ 6.0/10
9. [Google Research Spotlights Antigravity's /teamwork Multi-Agent Feature](#item-9) ⭐️ 6.0/10
10. [LinkedIn and Monster Remove Over 1,000 Fake Job Postings After CBC Probe](#item-10) ⭐️ 6.0/10
11. [FAA ground stop followed L3Harris telecom upgrade, Duffy says](#item-11) ⭐️ 6.0/10
12. [Microsoft restores Outlook, Teams and Copilot after day-long global outage](#item-12) ⭐️ 6.0/10
13. [Community-Made KDE Documentary Sparks Nostalgic Hacker News Thread](#item-13) ⭐️ 5.0/10
14. [Side-by-Side Comparison of All 13 Versions of The Secret of Monkey Island](#item-14) ⭐️ 5.0/10
15. [Italy fines Meta $887M over Android users' photo and video access](#item-15) ⭐️ 5.0/10
16. [Seeking Alpha Argues AI Is Finally Showing Up in the Economy](#item-16) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Lovable-built apps leak passports and 200K+ private messages via insecure Supabase defaults](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

Security researcher (HN user neathack) published research showing that apps built with the Lovable AI app builder expose highly sensitive user data — including passport details and more than 200,000 private messages — because of insecure default configurations, particularly around Supabase. The disclosure documents how these leaked records could be reached with little more than inspecting network calls in a browser, rather than any sophisticated attack. This is a concrete, high-impact example of a systemic pattern in AI-generated apps: non-technical builders ship public apps without understanding data exposure, so misconfigurations are replicated at scale rather than being one-off mistakes. It shifts the debate toward platform-level responsibility — whether Supabase's permissive defaults and Lovable's scaffolding should be deny-by-default before the next wave of vibe-coded apps goes live. The exposed data was reachable largely by observing network calls in the browser, meaning the barrier to exploitation is very low, and the affected apps are numerous and growing daily. Community commenters note that Supabase reportedly addressed related default-privilege issues around October 30, but there are reports that existing projects still retain the old, permissive defaults.

hackernews · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**Background**: Lovable is an AI app builder that turns natural-language prompts into full applications, including the interface, database and backend logic, with no coding required — an approach popularized as "vibe coding," a term coined by Andrej Karpathy in February 2025 for accepting AI-generated code without thorough review. Supabase is an open-source Firebase alternative that provides a Postgres database, auth and APIs, and its row-level security (RLS) rules are what actually determine who can read or write each table. Because such platforms ship permissive settings so that quick prototypes work out of the box, apps that never revisit those settings can end up with databases effectively open to anyone.

<details><summary>References</summary>
<ul>
<li><a href="https://supabase.com/docs/guides/api/securing-your-api">Securing your API | Supabase Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://axonbuild.com/blog/what-are-insecure-defaults/">What Are Insecure Defaults ? Supabase , Firebase, Lovable</a></li>

</ul>
</details>

**Discussion**: The thread (482 points, 174 comments) with the author present largely agrees the leaks are real but splits on blame: several commenters argue Supabase bears much of the culpability for a years-old deliberate tradeoff favoring easy onboarding, while others say Lovable deserves heat for building on those defaults. The dominant sentiment is that platforms need better safeguards — deny-by-default databases, least-privilege APIs and automated auth tests — with commenters comparing shipping such apps to flying a passenger plane without a license.

**Tags**: `#security`, `#AI-generated-code`, `#Supabase`, `#data-privacy`, `#vibe-coding`

---

<a id="item-2"></a>
## [SpaceX catches Super Heavy booster to close Starship Flight 15](https://x.com/i/broadcasts/2brajgZlOKRMka) ⭐️ 8.0/10

SpaceX's Starship Flight 15 ended with the Super Heavy booster being caught by the launch tower's mechanical arms, according to the broadcast and community reports. The operation marked another attempt at recovering the first-stage booster instead of letting it splash down in the ocean. Catching the booster is central to SpaceX's goal of turning Starship from a partially reusable rocket into a rapidly reusable launch system, which could lower costs and increase launch cadence. If the practice becomes routine, it would affect satellite operators, NASA's lunar plans, and the broader commercial space industry. The catch relies on the launch tower's giant "chopstick" arms and a precisely guided booster return, with grid fins steering the vehicle toward the tower. Coverage of Flight 15 has been inconsistent—some reports say the booster splashed down after a catch attempt—so the definitive outcome should be confirmed with SpaceX's official statement.

hackernews · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**Background**: Starship is SpaceX's next-generation launch system, consisting of the Super Heavy booster and the Starship upper stage, designed to carry more than 100 metric tonnes to orbit in a fully reusable configuration. Super Heavy is the first-stage booster; after separation, it returns toward the launch site. SpaceX's launch tower is equipped with mechanical arms—often called "chopsticks"—that can catch the booster instead of requiring landing legs, a step toward rapid reuse. Reusable launch vehicles aim to reduce cost by recovering and reflying hardware rather than discarding it.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://www.spacex.com/vehicles/starship">SpaceX - Starship</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-flight-15-chopsticks-double-catch-super-heavy-ship">SpaceX launches Starship on ambitious 22-hour Flight 15 test... | Space</a></li>

</ul>
</details>

**Discussion**: Commenters were overwhelmingly enthusiastic, calling the catch a historic engineering achievement and sharing personal stories about being inspired to study engineering or watching the launch with their children. The thread was more celebratory and emotional than technical, with little debate over costs or reusability trade-offs.

**Tags**: `#spacex`, `#starship`, `#reusable-rockets`, `#aerospace-engineering`, `#spaceflight`

---

<a id="item-3"></a>
## [Report: Nvidia CEO Jensen Huang Resigns; Trump Won't Raise Issue in China](https://www.cnbc.com/2026/11/13/trump-nvidia-huang-china.html) ⭐️ 8.0/10

According to the CNBC report, Nvidia CEO Jensen Huang resigned this week following reports of multiple affairs, including one with a woman described as a suspected Chinese spy named Alice Huang. Two Nvidia investors holding roughly $2.13 billion of stock as of June 30 are calling for a deliberate leadership search, and U.S. officials said President Trump does not plan to raise the Nvidia or espionage issue during an upcoming China trip. Nvidia is the central supplier of the AI accelerators underpinning most large-scale model training, so an abrupt CEO exit would shake investor confidence across the entire AI hardware supply chain. Because the story mixes corporate governance with espionage allegations, it also feeds directly into already tense U.S.-China technology and export-control politics. The item is brief and unverified: there is no cited confirmation from Nvidia's board, from Huang himself, or from regulators, so the resignation, the affair allegations and the spy claim should all be treated as reported-but-unconfirmed. The report also notes that Huang's exit has renewed scrutiny of Commerce Secretary Howard Lutnick and his family's financial ties to the chipmaker, a conflict-of-interest angle that could prove as consequential as the resignation itself.

rss · CNBC Top News · Nov 14, 15:36

**Background**: Nvidia designs the GPUs that power most AI data centers, which has made it one of the world's most valuable companies and a focal point of U.S. export controls on advanced chips sold to China. Jensen Huang co-founded the company in 1993 and has been its public face and CEO ever since, so his departure would be an unprecedented leadership change. The U.S. Commerce Department, led by Howard Lutnick, administers those chip export rules, which is why scrutiny of the secretary's ties to Nvidia carries policy weight.

**Tags**: `#Nvidia`, `#Jensen Huang`, `#China`, `#tech industry`, `#espionage`

---

<a id="item-4"></a>
## [Show HN: DeepSeek V3's core ideas rebuilt from scratch in ~200 lines of pure JAX](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) ⭐️ 7.0/10

Vaibhaav Tiwari published a GitHub project that reimplements DeepSeek V3's three distinguishing architectural ideas — Multi-head Latent Attention, mixture-of-experts load balancing via bias adjustment instead of an auxiliary loss, and multi-token prediction — in roughly 190-200 lines of pure JAX, accompanied by a full write-up with diagrams. The model is a small-scale 36.2M-parameter version trained on 207 old detective novels on a MacBook Air (24 GB) using jax-metal, running 12,000 steps in about 2.6 hours. DeepSeek V3 is a 671B-parameter Mixture-of-Experts model whose architectural tricks are usually buried in a long technical report and a huge codebase, so a few-hundred-line reimplementation makes a frontier design directly inspectable and hackable. For engineers trying to build intuition about modern LLM internals, this kind of first-principles educational artifact lowers the barrier far more than reading papers alone. The scope is deliberately tiny — 36.2M parameters, a 207-novel detective-fiction corpus, and laptop-scale training — so it is a learning artifact rather than a research contribution, and its outputs are not meant to be competitive. Community members also flagged that using an idiosyncratic dataset makes results harder to compare with other small-scale reproductions, and one commenter reported the project was the first to run end-to-end on an AMD RX 7600 XT 16GB under ROCm with JAX, needing the environment variable HSA_OVERRIDE_GFX_VERSION=11.0.0.

hackernews · VaibhaavTiwari · Nov 14, 15:04 · [Discussion](https://news.ycombinator.com/item?id=50497589)

**Background**: DeepSeek V3, released in late 2024, is an open-weight Mixture-of-Experts language model with 671B total parameters of which only about 37B are activated per token, and it was trained with roughly 2.788M H800 GPU hours. Mixture-of-Experts splits computation across specialized sub-networks ("experts") and uses a gating mechanism to route each token to only a few of them, which keeps inference cheap relative to total parameter count. Multi-head Latent Attention, introduced in DeepSeek-V2, compresses the key-value cache into a low-rank latent vector to cut inference memory. JAX is Google's NumPy-like numerical computing library with automatic differentiation and JIT compilation, and jax-metal is its Apple Metal backend for running on Mac GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V3-Base">deepseek -ai/ DeepSeek - V 3 -Base · Hugging Face</a></li>
<li><a href="https://memx.app/glossary/multi-head-latent-attention/">Multi - Head Latent Attention (MLA) Explained | MemX</a></li>

</ul>
</details>

**Discussion**: Reception was small but enthusiastic: commenters praised the first-principles reimplementation, with one saying there is "nothing like recreating a model from first principles" and another noting it rekindled interest in JAX. A less experienced developer asked for a learning roadmap for building intuition about inference and architecture, and one commenter suggested using commonly used datasets so results are comparable across projects, while the author explained the unusual dataset was a deliberate choice for variety.

**Tags**: `#jax`, `#deepseek-v3`, `#mixture-of-experts`, `#multi-head-latent-attention`, `#llm-implementation`

---

<a id="item-5"></a>
## [Google Project Zero moves to 90-day disclosure, with 60 and 30 days coming](https://projectzero.google/2026/11/disclosure-policy.html) ⭐️ 7.0/10

Google Project Zero announced a new "Full 90" disclosure policy effective immediately, publishing vulnerability details 90 days after the vendor is notified. The team has committed to a roadmap that shortens the deadline to "Full 60" on February 2, 2027, and then to "Full 30" on January 3, 2028. Project Zero's deadlines have long served as a de facto benchmark that other security teams and vendors reference, so compressing the window to 30 days could push the entire industry toward faster patching and tighter release cycles. Anyone shipping software that depends on upstream vendors or open-source maintainers will feel the pressure to respond to reports more quickly. The change is being rolled out as a staged, publicly announced timeline rather than a single abrupt shift, giving vendors roughly a year between each reduction. The policy governs the disclosure deadline itself, so the practical burden falls on projects that are resource-constrained — particularly open-source maintainers who lack dedicated security staff and must coordinate fixes across many downstream stakeholders.

hackernews · hacb · Nov 14, 11:13 · [Discussion](https://news.ycombinator.com/item?id=50496051)

**Background**: Project Zero is a team of Google security analysts founded in July 2014 to hunt for zero-day vulnerabilities — flaws unknown to the software's developers and therefore lacking a patch. Their long-standing practice has been to report bugs privately to vendors and then publish details after a fixed deadline, an approach known as coordinated vulnerability disclosure. The 90-day deadline became the team's best-known standard, and the debate ever since has been how much time vendors genuinely need to ship a fix versus how long users are left unknowingly exposed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Zero">Project Zero - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability</a></li>

</ul>
</details>

**Discussion**: Commenters were split on the timeline: one security researcher running 30-day disclosures at scale against major open-source projects argued that 90 days is far too long, while noting that cash-strapped OSS projects with many stakeholders are hard to coordinate with. Another commenter raised a different concern, warning that AI companies discovering bugs could exploit the disclosure process to pressure vendors into adopting their LLM products.

**Tags**: `#vulnerability-disclosure`, `#security`, `#project-zero`, `#open-source-security`, `#policy`

---

<a id="item-6"></a>
## [EFF: Tech Companies Are Trying to Redefine Privacy Again](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 7.0/10

The Electronic Frontier Foundation published a policy analysis arguing that technology companies are once again trying to shift the meaning of privacy, prompting a large Hacker News discussion about workplace AI recording and consent. Definitional shifts matter because they can weaken consent and legal protections just as AI meeting recorders make routine workplace surveillance easier and harder to refuse. The EFF item is an advocacy and policy analysis, not a technical disclosure, and the Hacker News thread (388 points, 151 comments) focused on concrete harms such as AI notetakers recording one-on-one meetings and the practical absence of an opt-out.

hackernews · gslin · Nov 14, 12:45 · [Discussion](https://news.ycombinator.com/item?id=50496602)

**Background**: The Electronic Frontier Foundation is a digital-rights nonprofit that has long focused on free expression, privacy, and surveillance. In workplace settings, AI notetakers can record and transcribe meetings, store audio, and generate summaries; legal guidance generally calls for advance notice and active consent, and portable devices can bypass company networks and approval rules. The dispute over what privacy means often determines whether such tools are treated as a consent problem, a data-security problem, or a fundamental civil-liberties issue.

<details><summary>References</summary>
<ul>
<li><a href="https://natlawreview.com/article/someone-recording-managing-workplace-risks-portable-ai-notetakers">Managing the Workplace Risks of Portable AI Notetakers</a></li>
<li><a href="https://www.recordinglaw.com/us-laws/ai-meeting-recording-laws/">AI Meeting Recording Laws by State: Complete Guide (2026)</a></li>
<li><a href="https://www.reedsmith.com/our-insights/blogs/employment-law-watch/102ls2n/the-legality-of-ai-powered-recording-and-transcription/">The legality of AI-powered recording and transcription</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly critical: one asked whether it is realistic to request that AI notetakers be turned off, another cited Article 12 of the UN Universal Declaration of Human Rights, and others recommended compartmentalized identities, air gaps, and supporting digital-rights litigation. A recurring view was that employees cannot meaningfully opt out without risking their jobs, and that companies treat no as negotiable.

**Tags**: `#privacy`, `#surveillance`, `#policy`, `#AI-notetakers`, `#EFF`

---

<a id="item-7"></a>
## [Blog Maps the Family Tree of Software Job Titles](https://zwischenzugs.com/2026/11/03/a-family-tree-of-software-job-titles/) ⭐️ 6.0/10

A blog post on zwischenzugs.com presents a family tree tracing how software job titles such as DevOps engineer, site reliability engineer, and Scrum Master have evolved and branched over time. The post prompted a Hacker News discussion about role ambiguity and whether these titles still carry clear meaning. Job titles shape hiring, compensation, and career expectations, so ambiguity around roles like DevOps and SRE can lead to mismatched responsibilities and inflated or diluted seniority signals. The discussion reflects broader industry churn as organizations reassess Agile ceremonies and operational ownership. The post is a reflective mapping rather than a formal taxonomy, and commenters noted it omits adjacent roles such as systems engineering and systems software engineering. Several practitioners said titles like DevOps engineer often describe a generalist who handles ambiguity and cloud infrastructure rather than a strictly defined discipline.

hackernews · umerf · Nov 14, 17:45 · [Discussion](https://news.ycombinator.com/item?id=50499038)

**Background**: DevOps is a practice that combines software development and IT operations to speed delivery through collaboration and automation, while site reliability engineering (SRE) applies software engineering to operations and reliability. Scrum Master is a facilitator role in Scrum, a lightweight Agile framework built around time-boxed sprints; the title is accountable for establishing Scrum and coaching the team.

<details><summary>References</summary>
<ul>
<li><a href="https://roadmap.sh/devops">DevOps Roadmap: Learn to become a DevOps Engineer or SRE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Site_reliability_engineering">Site reliability engineering - Wikipedia</a></li>
<li><a href="https://www.atlassian.com/agile/scrum/scrum-master">What is a Scrum Master? Role & Skills | Atlassian</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical that many software titles carry precise meaning: one called DevOps engineer a generalist role for people who can handle ambiguity, another said most organizations do not understand real DevOps, and several predicted titles will keep evolving rather than disappear. Some also criticized the chart for overlooking systems engineering and systems software engineering.

**Tags**: `#software engineering`, `#career`, `#job titles`, `#DevOps`, `#industry trends`

---

<a id="item-8"></a>
## [PyPI rolls out redesigned project pages highlighting provenance and security signals](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) ⭐️ 6.0/10

PyPI announced on November 6, 2026 that its redesigned project pages are now live, giving security signals such as provenance attestations from Trusted Publishing a prominent spot on each package's page. The new layout makes it easier to see at a glance whether a given release file carries a verifiable digital attestation. Making provenance visible to ordinary users turns an obscure supply-chain feature into something developers can actually act on when choosing dependencies, which should raise the baseline transparency of the Python packaging ecosystem. It also puts pressure on CI/CD providers to support the OIDC-based publishing flows that generate these attestations. Attestations are Sigstore-signed statements defined by PEP 740 that bind a distribution's hash to the CI workflow that uploaded it, and PyPI can display warnings when provenance metadata is missing, incomplete, or inconsistent with a project's history. Notably, this detects compromised uploads of previously benign projects rather than flagging projects that were malicious from the start, and Trusted Publishing still lacks support for reusable workflows.

hackernews · rbanffy · Nov 14, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50497892)

**Background**: Trusted Publishing lets maintainers register a specific CI workflow, such as a GitHub Actions job, as the only allowed publisher, so no long-lived PyPI API token is needed. Instead of a static key, the build environment proves its identity with a short-lived OpenID Connect token, and the resulting record is a Sigstore-based digital attestation. Provenance is that record: a verifiable statement of where a release file came from and how it was built, per PEP 740.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pypi.org/using-pypi/package-security/provenance/">Checking Provenance (package origin) - PyPI Docs</a></li>
<li><a href="https://docs.pypi.org/trusted-publishers/using-a-publisher/">Publishing with a Trusted Publisher - PyPI Docs</a></li>
<li><a href="https://pypi.org/project/pypi-attestations/">pypi-attestations</a></li>

</ul>
</details>

**Discussion**: Commenters broadly welcomed the visibility but raised concerns: one argued the trust model pushes everyone toward big-cloud CI providers and creates lock-in, another clarified that it detects hacked uploads rather than malicious projects by design, and others asked for Trusted Publishing support for reusable workflows while praising keyless Sigstore-style signing.

**Tags**: `#python`, `#pypi`, `#supply-chain-security`, `#sigstore`, `#trusted-publishing`

---

<a id="item-9"></a>
## [Google Research Spotlights Antigravity's /teamwork Multi-Agent Feature](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 6.0/10

Google Research published a blog post showcasing Antigravity's /teamwork feature applied to math, science, engineering, and coding tasks, presenting example workflows rather than a new launch. In the Hacker News thread, Google's Mirrokni clarified that parts of /teamwork were already announced on the Antigravity blog, and that this post was meant to report advances and showcase what users can do with it. Multi-agent orchestration is becoming the main competitive battleground among agentic coding platforms, so Google's messaging around /teamwork signals how it intends to position Antigravity against Claude Code and Codex-style dynamic workflows. How convincingly these features work on real science and engineering tasks will shape developer adoption of Google's agent-first tooling. The post is largely a showcase of task examples, and commenters noted there is no published comparison or benchmark against competing multi-agent harnesses. Critics also pointed out missing conveniences such as an auto mode, and that a related /goal capability was announced well after similar features existed in Claude Code and Codex.

hackernews · acossta · Nov 14, 13:20 · [Discussion](https://news.ycombinator.com/item?id=50496811)

**Background**: Google Antigravity is Google's agentic development platform, announced in November 2025, which pairs a familiar AI-assisted coding experience with an agent-first interface where agents plan and execute multi-step tasks. An agent harness (or scaffolding) is the software layer surrounding a large language model that drives tool calls, manages context, and keeps an agent progressing through a task. Multi-agent collaboration, where several role-specialized agents work on different parts of a problem, is an active research area in LLM systems and is now being productized inside coding tools.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/">Build with Google Antigravity, our new agentic development ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2501.06322">[2501.06322] Multi-Agent Collaboration Mechanisms: A Survey ... A survey on LLM-based multi-agent systems: workflow ... LangGraph: Multi-Agent Workflows - LangChain Blog A Survey of Multi-AI Agent Collaboration: Theories ... LLM-Powered Multi-Agent Systems: A Survey of Collaboration ... LLM-Guided Multi-Agent Collaboration for Complex Task ...</a></li>

</ul>
</details>

**Discussion**: Reaction on Hacker News was mixed: some developers shared related multi-agent research and reported that team-based, role-based workflows deliver more autonomy with less quality loss, and one commenter enthused about the R&D acceleration this could enable. Others were skeptical, arguing it is unclear how /teamwork differs from Claude's dynamic workflows, that Antigravity feels behind as a harness, and that the post does not actually explain how to use the feature.

**Tags**: `#AI agents`, `#multi-agent systems`, `#Google Antigravity`, `#LLM workflows`, `#developer tools`

---

<a id="item-10"></a>
## [LinkedIn and Monster Remove Over 1,000 Fake Job Postings After CBC Probe](https://www.cbc.ca/news/canada/linkedin-monster-take-down-over-1-000-fake-job-postings-after-cbc-investigation-9.7415379) ⭐️ 6.0/10

Following a CBC investigation, LinkedIn and Monster have taken down more than 1,000 fraudulent job postings that had been listed on their platforms. The takedowns mark a rare public acknowledgment that fake listings are widespread enough to require bulk removal rather than case-by-case moderation. Job platforms are a primary gateway to employment for millions of people, so fake postings expose job seekers to identity theft, financial fraud and lost time at exactly the moment they are most vulnerable. The scale of the takedown also raises questions about how much undetected fraudulent activity remains on platforms that function as gatekeepers of the hiring market. The removals came only after a news investigation prompted the platforms to act, suggesting that existing automated and manual screening did not catch these listings on its own. The reports do not detail how the fraudulent postings evaded detection or whether the accounts behind them were also banned.

hackernews · gnabgib · Nov 14, 18:56 · [Discussion](https://news.ycombinator.com/item?id=50499723)

**Background**: Fake job listings typically impersonate real employers or invent plausible companies in order to harvest applicants' personal data — such as resumes, government ID numbers or bank details — or to recruit victims as unwitting money mules. They spread easily because legitimate hiring increasingly happens entirely online, and because platforms are incentivized to maximize the number of listings rather than to verify each one. Trust-and-safety teams usually rely on a mix of automated classifiers, user reports and manual review, all of which can be overwhelmed at scale.

**Discussion**: Commenters were broadly cynical about the scale of online fraud, with one citing reports that a large share of Meta's ad revenue comes from scam-related advertising and asking how much of the wider economy runs on deception. Others shared personal experiences of recruiter spam traced back to old public job-seeking posts, and several voiced frustration that social networks have become an unavoidable gatekeeper for employment — including one who said 15 years of applying via LinkedIn never produced a job.

**Tags**: `#trust-and-safety`, `#job-market`, `#fraud`, `#platform-moderation`, `#linkedin`

---

<a id="item-11"></a>
## [FAA ground stop followed L3Harris telecom upgrade, Duffy says](https://www.cnbc.com/2026/11/14/faa-ground-stop-flights-resume-delays.html) ⭐️ 6.0/10

Transportation Secretary Sean Duffy said the FAA's nationwide ground stop on Nov. 13 followed upgrade work by L3Harris Technologies on an older telecommunications system, including maintenance to switch from copper wire to fiber. Flight disruptions continued into the weekend as airlines worked to recover. The incident shows how a maintenance change in aging critical communications infrastructure can halt nationwide air travel, affecting airlines and passengers and drawing scrutiny to the FAA's managed-services contract with L3Harris. It also highlights the operational risks involved in modernizing systems that air traffic control depends on. Duffy described the U.S. telecommunications system as "incredibly old" and said the copper wire was being discontinued, while L3Harris said it is supporting the FAA's investigation. No final root cause has been confirmed, and the incident remains under investigation.

rss · CNBC Top News · Nov 14, 18:32

**Background**: The FAA Telecommunications Infrastructure (FTI) program is a managed-services contract under which L3Harris owns equipment and leases telecommunications services to transmit voice, data and video for the National Airspace System; L3Harris is replacing decades-old copper connections with modern high-speed networks across FAA facilities. A ground stop is an FAA order requiring aircraft to remain on the ground and barring them from taking off, while planes already in the air are usually allowed to continue. Because air traffic control depends on reliable communications links among major control centers, radar sites and weather stations, work on that underlying network can have nationwide effects.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/14/faa-ground-stop-flights-resume-delays.html">Ground stop followed contractor upgrade to L 3 Harris telecom system ...</a></li>
<li><a href="https://www.bbc.com/news/articles/c6wy9lynq4qno">Copper wire upgrade caused nationwide flight chaos, US transport...</a></li>
<li><a href="https://www.l3harris.com/all-capabilities/faa-telecommunications-infrastructure-fti">FAA Telecommunications Infrastructure (FTI) - L3Harris</a></li>

</ul>
</details>

**Tags**: `#FAA`, `#aviation systems`, `#telecom outage`, `#L3Harris`, `#critical infrastructure`

---

<a id="item-12"></a>
## [Microsoft restores Outlook, Teams and Copilot after day-long global outage](https://www.bbc.co.uk/news/articles/c6rrg51rkz09o?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

Microsoft said it fully restored Outlook, Teams, Copilot and other Microsoft 365 services after a global outage that stretched across Thursday and Friday and disrupted millions of users, organizations and businesses worldwide. The company said it had "addressed the underlying issue" and issued an apology, describing itself as "deeply sorry" for the disruption. Outlook, Teams and Microsoft 365 are core productivity infrastructure for a large share of the world's businesses and governments, so a day-long failure cascades into missed communications and stalled workflows far beyond Microsoft's own customers. Experts quoted in coverage warn the incident exposes Australia's reliance on foreign technology, with costs potentially reaching into the billions of dollars and some small businesses at risk of closure. The outage affected Outlook, Teams and Microsoft 365 throughout Thursday and Friday, and Microsoft has not publicly detailed the specific technical root cause, describing it only as an "underlying issue" with an unspecified service. The incident is being framed as an economic event as much as a technical one, with estimated multi-billion-dollar costs and calls to examine concentration risk in cloud dependencies.

rss · BBC Business · Nov 14, 06:42

**Background**: Microsoft 365 is the subscription bundle that includes Outlook for email, Teams for chat and meetings, and the Office apps such as Word and Excel, while Copilot is Microsoft's AI assistant layered on top of those products. Because these tools are delivered as cloud services rather than software installed on a local machine, a failure in a shared backend component can take down many products simultaneously for every customer at once. This kind of single-point-of-failure dynamic is why major cloud outages at providers like Microsoft, Google or AWS often become global events rather than isolated incidents.

**Tags**: `#Microsoft`, `#global outage`, `#cloud services`, `#Outlook`, `#Copilot`

---

<a id="item-13"></a>
## [Community-Made KDE Documentary Sparks Nostalgic Hacker News Thread](https://tube.kockatoo.org/w/fFinNHfanLT7aBEb2B8y4c) ⭐️ 5.0/10

A community-produced documentary tracing the history and evolution of the KDE desktop environment has been published on the PeerTube instance tube.kockatoo.org. The video was accompanied by a Hacker News discussion that reached roughly 320 points and 69 comments, many from users with decades of experience on KDE. The documentary preserves the oral and technical history of one of the longest-running free software desktop projects, showing how a 1996 Usenet call for volunteers grew into an ecosystem used by millions. It also highlights the cultural side of open source — how a decentralized, volunteer community sustains a large C++ codebase and Qt-based stack for nearly three decades. The news itself is a documentary film rather than a software release, so there is no version number or technical change to evaluate; the value lies in the historical narrative and first-hand accounts. The HN thread mixes nostalgia with criticism, particularly around the troubled KDE 4 transition, and notes that individual KDE applications like Dolphin and Konsole still retain users who have moved to other desktops or window managers.

hackernews · mrkn1 · Nov 14, 13:43 · [Discussion](https://news.ycombinator.com/item?id=50496976)

**Background**: KDE began in 1996 as the "K Desktop Environment", and its 1.0 release shipped in July 1998; the umbrella "KDE Software Compilation" was later split into three independently released products: KDE Plasma, KDE Frameworks and KDE Applications. KDE is built on Qt, a cross-platform C++ application framework available under both commercial licenses and open-source GPL/LGPL terms, which in its early years was a major source of both capability and licensing tension for the project. Today the KDE community maintains more than 200 applications that run on essentially any Linux desktop and often on other platforms too.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KDE_Desktop_Environment">KDE Desktop Environment</a></li>
<li><a href="https://en.wikipedia.org/wiki/KDE">KDE - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qt_framework">Qt framework</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly affectionate and reflective: one described using KDE for close to two decades since the 3.x era and still relying on Dolphin and Konsole, while another praised KDE as a fascinating case study in the difficulty of building software that works for most people. Several recalled the project's earliest days, including the original Usenet post seeking volunteers for a "Kool Desktop Environment", and the enthusiasm around early betas. The mood was tempered by criticism of KDE 4's instability, with some users saying they drifted away after that release.

**Tags**: `#KDE`, `#open-source`, `#Linux desktop`, `#documentary`, `#community history`

---

<a id="item-14"></a>
## [Side-by-Side Comparison of All 13 Versions of The Secret of Monkey Island](https://monkeyisland.pages.dev/) ⭐️ 5.0/10

A new website at monkeyisland.pages.dev presents a visual side-by-side comparison of all 13 released versions of Lucasfilm Games' 1990 point-and-click adventure The Secret of Monkey Island, spanning CGA, EGA, VGA, Hercules monochrome, Amiga, Atari ST, FM Towns, CD-ROM and Special Edition releases. The site itself is styled after Borland Turbo Vision, the character-based UI toolkit common in DOS applications of the era. The comparison is a compact record of how the same artistic intent was re-authored for wildly different display hardware, from four-colour CGA to 256-colour VGA, which makes it a useful reference for game-preservationists and pixel artists studying constrained art. Its popularity on Hacker News (roughly 440 points and 140 comments) shows that early-PC graphics history still resonates strongly with the developer community. CGA limited the palette to four colours (cyan, magenta, white and black) at 320×200, EGA expanded this to 16 simultaneous colours while largely keeping CGA-era resolution and refresh rates, and VGA introduced 256 colours on screen. The comparison also surfaces subtler differences between releases, such as the smoother scrolling of the FM Towns port and small animation changes between the floppy and CD-ROM versions.

hackernews · maximilianburke · Nov 14, 04:23 · [Discussion](https://news.ycombinator.com/item?id=50493904)

**Background**: The Secret of Monkey Island was developed and published by Lucasfilm Games in 1990 and ran on the SCUMM engine (Script Creation Utility for Maniac Mansion), the in-house scripting system that powered most LucasArts adventure games until the company moved to the GrimE engine with Grim Fandango in 1998. Because the game was ported to many platforms and re-released on floppy, CD-ROM and later as a Special Edition, each version had to be redrawn or recoloured for its target hardware, which is why 13 distinct renditions exist.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SCUMM">SCUMM - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Video_Graphics_Array">Video Graphics Array - Wikipedia</a></li>
<li><a href="https://scummbar.com/game/the-secret-of-monkey-island/versions">The Secret of Monkey Island Versions — The Monkey Island ...</a></li>

</ul>
</details>

**Discussion**: Commenters were largely nostalgic: several recalled the cold, alien feel of CGA's cyan-and-magenta palette and the warmth that EGA/VGA brought, while others praised the artists who produced recognisable scenes from four colours or a low-resolution monochrome Hercules display. Others shared memories of Amiga multi-floppy disk swapping and the notorious Monkey Island 2 copy protection that only appeared partway through the game.

**Tags**: `#retro-gaming`, `#graphics`, `#game-preservation`, `#nostalgia`, `#dos`

---

<a id="item-15"></a>
## [Italy fines Meta $887M over Android users' photo and video access](https://www.cnbc.com/2026/11/14/italy-fines-meta-887-million-over-android-users-data-access.html) ⭐️ 5.0/10

Italy has fined Meta Platforms $887 million, alleging that the company accessed Android users' photographs and videos without obtaining consent or notifying them. According to the report, roughly 20 million users in Italy were affected by the practice without being informed that Meta had access to their photos. This is one of the largest privacy-related penalties ever levied against a major platform in Europe, and it signals that national regulators are willing to act independently of Brussels on data-protection issues. It could push Meta and other app developers to rework how they request and disclose media access on Android, and it raises the stakes for any service that quietly broadens its data collection on mobile devices. The penalty concerns access to photos and videos specifically, and the case is notable for the scale cited — about 20 million affected users in a single country. Meta has historically contested such decisions and typically appeals; the exact legal basis and whether the fine is final are not specified in the available reporting.

rss · CNBC Top News · Nov 14, 18:49

**Background**: Android's permission model has tightened considerably over the years to limit how apps reach user media. Android 10 introduced scoped storage, which restricts apps to their own files and to media they are explicitly granted; Android 13 replaced the broad READ_EXTERNAL_STORAGE permission with separate READ_MEDIA_IMAGES and READ_MEDIA_VIDEO permissions; and Android 14 added partial photo and video access, letting users share only selected items. Regulators scrutinize whether apps request these permissions transparently and whether data already accessible through broader legacy paths is used without clear disclosure.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/about/versions/14/changes/partial-photo-video-access">Grant partial access to photos and videos - Android Developers</a></li>
<li><a href="https://developer.android.com/training/data-storage/shared/media">Access media files from shared storage | App data and files | Android ...</a></li>
<li><a href="https://support.google.com/googleplay/android-developer/answer/15800983?hl=en">Required actions to comply with our Photo & Video Permissions ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#regulation`, `#Meta`, `#Android`, `#data-protection`

---

<a id="item-16"></a>
## [Seeking Alpha Argues AI Is Finally Showing Up in the Economy](https://seekingalpha.com/article/4968202-ai-is-finally-showing-up-in-economy?source=feed_all_articles) ⭐️ 5.0/10

A Seeking Alpha article argues that artificial intelligence is finally beginning to appear in the broader economy as a measurable force, rather than remaining a purely speculative technology theme. The piece is a macro-level financial analysis rather than a product or research announcement, so no specific model release, version number, or corporate event is attached to it. If AI investment and adoption begin to register in macro data such as productivity, capital expenditure, and corporate earnings, it would shift how investors and policymakers judge whether the massive spending on AI infrastructure is paying off. That would extend AI's influence well beyond big technology companies into valuations and business decisions across the wider market. The core difficulty the article faces is attribution: separating AI's contribution from other drivers of growth, cyclical effects, and long adoption lags is inherently difficult, and the available excerpt contains no underlying figures or methodology that could be independently verified. Readers should therefore treat the claim as an argument to be evaluated rather than an established statistical finding.

rss · Seeking Alpha · Nov 14, 15:53

**Background**: Economists have long debated the so-called productivity paradox, the observation associated with Robert Solow that computers could be seen everywhere except in the productivity statistics; general-purpose technologies such as electricity and the internet took decades to translate into measured output gains. AI is widely treated as another such general-purpose technology, with enormous sums currently flowing into data centers, chips, and model training. The question the article addresses is whether that spending has now grown large enough, and the technology capable enough, to leave a visible trace in aggregate economic data rather than only in the revenue of a handful of suppliers.

**Tags**: `#AI economics`, `#macroeconomics`, `#technology adoption`, `#financial analysis`, `#AI impact`

---

