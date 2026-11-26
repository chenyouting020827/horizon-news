# Horizon Daily - 2026-11-26

> From 151 items, 19 important content pieces were selected

---

1. [OpenAI preprint claims matrix multiplication exponent is exactly 9/4](#item-1) ⭐️ 9.0/10
2. [1Password Discloses Incident Involving Malicious Code Pushed to Backend](#item-2) ⭐️ 8.0/10
3. [Community shrinks Anthropic's 17M-line Lean GRH proof to 76k lines](#item-3) ⭐️ 8.0/10
4. [Preprint Claims to Disprove the Polynomial Hirsch Conjecture](#item-4) ⭐️ 8.0/10
5. [Google Research posts "Cogentic" papers on factoring and discrete logs](#item-5) ⭐️ 8.0/10
6. [US regulators approve SpaceX's million-satellite Starmind AI constellation](#item-6) ⭐️ 8.0/10
7. [Ubuntu's Slow Security Patches Spark Debian Migration Debate](#item-7) ⭐️ 7.0/10
8. [NFS2ROOT: 12-year-old pre-auth root bug in Linux kernel NFS server](#item-8) ⭐️ 7.0/10
9. [Developer reverse-engineers Windows loudness equalization and ports it to PipeWire](#item-9) ⭐️ 7.0/10
10. [Blogger Audits Clojure's Core Library with Lean, Reports Unreported Bugs](#item-10) ⭐️ 7.0/10
11. [New York Times Warns Photographers Against Updating Photoshop Over AI Features](#item-11) ⭐️ 6.0/10
12. [Hobbyist runs tiny Qwen LLM on bare metal in pure assembly, no OS](#item-12) ⭐️ 6.0/10
13. [Blogger Claims TypeSafe's 'Jev' Is Actually Qwen3.5-35B-A3B](#item-13) ⭐️ 6.0/10
14. [US stocks slide as AI fears intensify, Nasdaq drops nearly 4%](#item-14) ⭐️ 6.0/10
15. [Hera images reveal stadium-sized crater from NASA's DART asteroid impact](#item-15) ⭐️ 6.0/10
16. [Huawei guilty of stealing US trade secrets, acquitted of racketeering](#item-16) ⭐️ 6.0/10
17. [BBC Analysis: Jensen Huang Has Made Himself Irreplaceable at Nvidia](#item-17) ⭐️ 5.0/10
18. ['Paris Manifesto' Open Letter Urges Democracies to Counter AI-Era Extreme Wealth](#item-18) ⭐️ 5.0/10
19. [University of Sydney makes oral defence mandatory for all honours theses to counter AI](#item-19) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [OpenAI preprint claims matrix multiplication exponent is exactly 9/4](https://scottaaronson.blog/?p=10379) ⭐️ 9.0/10

A preprint dated November 24, 2026 from OpenAI, titled "The matrix multiplication exponent is nine fourths," argues that the exponent ω governing the asymptotic cost of multiplying square matrices equals 9/4 (2.25) over any field — and, unusually, claims a matching lower bound rather than only a faster algorithm. Scott Aaronson amplified the result on his blog with a post whose title is essentially repeated profanity, and the linked Hacker News thread drew hundreds of comments. If correct, this would close one of the longest-running open problems in algebraic complexity theory and overturn the assumption that ω is unknown somewhere between 2 and the long-standing ~2.37 upper bound. Because fast matrix multiplication underpins many algorithmic and cryptographic constructions, a proven exact value — and the proof techniques behind it — could ripple through complexity theory, algorithm design, and how the field thinks about lower bounds in general. The paper claims ω = 9/4 over any field, and reporting on it notes that parts of the argument are covered by Lean formalization while other parts still require independent verification by researchers. The claim is a preprint, not a peer-reviewed result, and the Hacker News thread includes unverified rumors about related fast-factoring work, so the exact scope of what has been machine-checked versus asserted remains a key question.

hackernews · Kotlopou · Nov 25, 19:11 · [Discussion](https://news.ycombinator.com/item?id=50646108)

**Background**: The matrix multiplication exponent ω is defined as the smallest number such that two n×n matrices can be multiplied in roughly O(n^ω) operations. Strassen's 1969 algorithm beat the naive O(n^3) bound, and decades of work — culminating in Coppersmith–Winograd and later refinements around 2.371552 — pushed the best known upper bound steadily downward, while the only obvious lower bound was the trivial 2. Proving an exact value of ω has long been considered far out of reach, which is why a claimed matching lower bound attracts this much attention; Lean and MathLib are proof-assistant tools that let mathematicians machine-check proofs, and they feature prominently in discussions of how much credit the AI system deserves.

<details><summary>References</summary>
<ul>
<li><a href="https://kingy.ai/blog/openai-matrix-multiplication-exponent-nine-fourths/">OpenAI Claims Matrix Multiplication Exponent Is Exactly 9/4</a></li>
<li><a href="https://xenospectrum.com/en/matrix-multiplication-nine-fourths-lower-bound/">OpenAI Preprint Claims the Matrix Multiplication Exponent Is ...</a></li>
<li><a href="https://raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">The matrix multiplication exponent is nine fourths</a></li>

</ul>
</details>

**Discussion**: Commenters treated the result as potentially paradigm-shifting but were sharply divided on interpretation: one invoked Bruno Latour's "centers of calculation" to argue that data-organizing infrastructure like Lean/MathLib, not LLMs, may deserve the credit, while another worried about P vs NP and fast factoring threatening RSA. Others reached for historical analogies, comparing the moment to late-19th-century physicists who thought their field was "solved" just before quantum mechanics, and some expressed ambivalence about a future in which AI dispatches the major open problems.

**Tags**: `#theoretical-computer-science`, `#matrix-multiplication`, `#complexity-theory`, `#ai-for-math`, `#research-breakthrough`

---

<a id="item-2"></a>
## [1Password Discloses Incident Involving Malicious Code Pushed to Backend](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password published a blog update disclosing a security incident in which malicious code was pushed to its backend services, prompting a large Hacker News thread (over 1,100 points and 480 comments). The announcement outlined action items but, according to commenters, did not clearly explain how the code push was possible or whether branch-protection rules were missing or bypassed. The incident highlights the dominant attack path against SaaS providers: compromise an employee laptop, push code to the repository, and let normal deployment carry the attacker into production. For a password manager, that raises the worst-case scenario of malicious client or server code exfiltrating decrypted secrets, which is why the discussion extends well beyond 1Password itself. Commenters noted that 1Password's end-to-end encrypted vault design and the Secret Key provide a layer of mitigation, since an attacker who only reaches backend services still cannot decrypt vault data without also compromising client-side secrets. Still, critics argued the write-up omitted key forensic details, such as whether push-to-main was restricted, how the malicious code was detected, and an explicit statement that users' encrypted vaults were not downloaded.

hackernews · lxhrstn · Nov 25, 17:18 · [Discussion](https://news.ycombinator.com/item?id=50644817)

**Background**: 1Password is a widely used password manager that can store vaults in the cloud and sync them across devices, so its backend services are part of the trust chain for millions of users. In modern SaaS development, engineers with repository access can push code that is automatically built and deployed, which is why controls like GitHub branch protection rules—requiring reviews and passing status checks before merging to main—are considered baseline defense. When those guardrails fail or are bypassed, a single compromised developer machine can turn into a full supply-chain compromise of the service.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Protected_branches_GitHub">Protected branches (GitHub)</a></li>

</ul>
</details>

**Discussion**: The dominant sentiment was concern rather than panic: security researcher tptacek called this the single most important attack vector for SaaS companies, noting that as headcount grows the odds of one compromised laptop approach one. Others pushed back on the disclosure's completeness—ctidd asked whether push-to-main was simply unprotected, fn-mote wanted an explicit statement that encrypted vaults were not downloaded, and a long-time user keeping a local-only vault said this is exactly the scenario they feared. K0nserv added a related worry that passkey implementations, and passkeys stored inside 1Password, can end up weaker than a password plus an external second factor.

**Tags**: `#security`, `#1Password`, `#supply-chain`, `#SaaS`, `#incident-response`

---

<a id="item-3"></a>
## [Community shrinks Anthropic's 17M-line Lean GRH proof to 76k lines](https://github.com/lsernau/grh-lean) ⭐️ 8.0/10

A community project (lsernau/grh-lean) has released a drastically shortened Lean formalization of the Generalized Riemann Hypothesis proof that Levent Alpöge produced with Anthropic's Claude, cutting the original ~17 million lines across 175,187 files down to roughly 76,000 lines — a 99.56% reduction. The shortened version adds human-readable documentation throughout and explicitly separates "known math" from "new math." The original formal proof was so large that essentially no human could review it, so compressing it into a readable artifact directly addresses the concern that AI-generated proofs are opaque and unverifiable in practice. This makes the GRH formalization inspectable by mathematicians and strengthens the case that AI-assisted formal proving can produce results the community can actually digest. The shortened proof claims to rely only on the standard Lean axioms propext, Classical.choice and Quot.sound, and the repository organizes the material so readers can see which parts are established mathematics versus genuinely new argument. It remains a refinement of Alpöge's original work rather than an independent proof, and reading it still assumes familiarity with Lean 4 and mathlib conventions.

hackernews · nb-t · Nov 25, 21:48 · [Discussion](https://news.ycombinator.com/item?id=50648050)

**Background**: The Riemann Hypothesis, and its generalization to Dirichlet L-functions (GRH), is among the most important open conjectures in mathematics, stating that all non-trivial zeros of these functions lie on a line with real part 1/2. In November 2026 Levent Alpöge announced a proof found with Anthropic's Claude, released as a Lean 4 formal proof so that correctness could be machine-checked. Lean is an open-source proof assistant in which proofs are written as code and verified by a small trusted kernel; because automated and AI-assisted proofs can be enormous, the gap between "machine-verified" and "human-understandable" has become a central debate, notably raised by Terence Tao.

<details><summary>References</summary>
<ul>
<li><a href="https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/">Alpöge/Claude proof of the Generalized Riemann Hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the readability gains, noting the clear known-math versus new-math split and inline documentation, and highlighted the 99.56% reduction from ~17M to ~76k lines. A recurring thread asked whether LLM "proof golfing" plus explanation answers Terence Tao's concern about huge, insight-free proofs, while others requested an accessible explanation for mathematicians who don't read Lean — particularly what reliance on the axioms propext, Classical.choice and Quot.sound actually means.

**Tags**: `#Lean`, `#formal verification`, `#mathematics`, `#AI-assisted proving`, `#proof assistants`

---

<a id="item-4"></a>
## [Preprint Claims to Disprove the Polynomial Hirsch Conjecture](https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf) ⭐️ 8.0/10

A preprint posted to OpenAI's public math repository on GitHub claims to construct simple polytopes whose edge-vertex graph diameter grows superpolynomially, which would refute the polynomial Hirsch conjecture. If the construction holds up, it means no pivot rule can make the simplex method run in polynomial time on all linear programs. The result would close a question left open since Francisco Santos disproved the original Hirsch conjecture in 2010, and it removes the last hope that polytope diameter explains why the simplex method behaves so well in practice. It also draws attention because it appears in OpenAI's math preprint repository, fueling speculation about AI-assisted proof work. The claim requires independent verification since it is an unrefereed preprint, and it applies to simple polytopes — those where exactly d facets meet at every vertex. Commenters note it is a refinement of Santos's 2010 counterexample rather than a paradigm shift, since the original conjecture was already known to be false.

hackernews · acossta · Nov 25, 17:34 · [Discussion](https://news.ycombinator.com/item?id=50644980)

**Background**: The Hirsch conjecture, posed by Warren Hirsch in a 1957 letter to George Dantzig, stated that the graph of a d-dimensional polytope with n facets has diameter at most n − d — that is, you can walk between any two vertices in at most n − d steps along edges. The conjecture mattered because this diameter lower-bounds the number of steps the simplex method takes for linear programming, offering a possible explanation for its speed in practice. In 2010 Francisco Santos disproved it with a 43-dimensional polytope with 86 facets and diameter greater than 43, but that counterexample left open whether the diameter is at least polynomial in n and d; the polynomial Hirsch conjecture asserts that it is.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Polynomial_Hirsch_conjecture">Polynomial Hirsch conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hirsch_conjecture">Hirsch conjecture - Wikipedia</a></li>
<li><a href="https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n1-p07-p.pdf">A counterexample to the Hirsch Conjecture - Annals of Mathematics</a></li>

</ul>
</details>

**Discussion**: Commenters broadly accept the framing: one offers a plain-English analogy of linear programs as multi-dimensional shapes where every corner is a valid but not necessarily optimal solution, while another stresses that this only rules out polynomial-time simplex algorithms and is more of a mopping-up result. Others speculate about an imminent 'post-math' era of AI-solved problems, joke that breakthroughs now arrive as GitHub patch notes, and ask how anyone finds one paper among a thousand in the repository.

**Tags**: `#mathematics`, `#linear-programming`, `#complexity-theory`, `#polytopes`, `#simplex-algorithm`

---

<a id="item-5"></a>
## [Google Research posts "Cogentic" papers on factoring and discrete logs](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 8.0/10

Google Research has published a folder of "Cogentic" research papers in its public google-research GitHub repository, with titles covering integer factorization, discrete logarithms and related problems such as edge reconstruction. The drop is a bare collection of PDFs with no accompanying announcement, and by the time it hit the front page of Hacker News it had drawn 443 points and 332 comments of speculation about cryptographic and AI-for-mathematics implications. Integer factorization and the discrete logarithm problem are the hardness assumptions underpinning RSA, Diffie–Hellman and ElGamal-style public-key cryptography, so any credible progress on them is read as a potential threat to widely deployed security. The release also feeds a broader narrative that AI systems are beginning to make real progress on open mathematical problems, which is why a simple repository link generated outsized attention. The submitted item is only a directory of PDFs (for example cogentic_research_papers/edge_reconstruction/paper.pdf) with no abstract, benchmark or claim of breaking any cryptosystem, and community descriptions of Cogentic say it is an orchestration harness that lets existing LLMs collaborate on mathematical conjectures through a central orchestrator and a shared database of intermediate proofs. Readers should treat the cryptographic framing as speculation rather than a demonstrated result.

hackernews · rgwohlbold · Nov 25, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50642086)

**Background**: Public-key cryptography such as RSA rests on the assumption that factoring a large semiprime into its prime factors is computationally infeasible, while Diffie–Hellman and ElGamal rest on the analogous difficulty of computing discrete logarithms in carefully chosen groups. An efficient general algorithm for either problem would render those schemes insecure, which is why factorization and discrete-log announcements attract intense scrutiny. In parallel, LLM-based systems have recently been applied to open mathematics problems, prompting comparisons to AlphaGo's exploration of Go's enormous search space.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50642086">Google releases Cogentic papers on integer... | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Integer_factorization">Integer factorization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_logarithm_problem">Discrete logarithm problem</a></li>

</ul>
</details>

**Discussion**: Commenters were split between excitement and caution: one cited "credible people" rumoring that this is the tip of something larger (linking to a post by Aran Nayebi), while others framed the wave of results as an AlphaGo-style search-space story and argued it has never been a more exciting time to study computer science. Several noted the odd contrast between daily mathematical breakthroughs and a sliding AI market, and one said the recent run of results on problems like Navier–Stokes and the Riemann Hypothesis has changed their belief that mathematics was immune to simply throwing money at problems.

**Tags**: `#cryptography`, `#integer-factorization`, `#ai-for-math`, `#google-research`, `#hackernews-discussion`

---

<a id="item-6"></a>
## [US regulators approve SpaceX's million-satellite Starmind AI constellation](https://www.bbc.co.uk/news/articles/cwp836l8n1jgo?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

US regulators have approved SpaceX's plan to deploy Starmind, a constellation of up to one million satellites intended to deliver AI computing capacity from orbit. SpaceX positions Starmind as the most cost- and energy-efficient way to meet surging demand for AI compute, with the first satellite design designated AI1. If even a fraction of the constellation is built, it would dwarf every existing satellite network and shift part of the AI infrastructure build-out from power-constrained terrestrial data centers into orbit. The approval also sets an early regulatory precedent for space-based AI computing, with knock-on effects for energy policy, launch economics and orbital-debris governance. The decision is a regulatory green light rather than a launch commitment, and the filings cover an upper bound of one million satellites — orders of magnitude beyond the roughly 9,000 Starlink satellites launched so far. Orbital AI data centers still face open engineering questions around heat rejection, inter-satellite and downlink bandwidth, and maintenance, and their economics hinge on continued steep reductions in launch costs.

rss · BBC Business · Nov 26, 00:07

**Background**: Starmind is a planned constellation of solar-powered, space-based AI data center satellites being developed by SpaceX, joining Starship, Starlink, Starshield and Starbase in the company's naming scheme. Orbital data centers are a proposed concept for building AI computing infrastructure in sun-synchronous or other orbits, drawing on space-based solar power for near-continuous energy. The idea has roots in military space architectures such as the 1980s Brilliant Pebbles program and the Space Development Agency's Proliferated Warfighter Space Architecture, which envisioned autonomous on-orbit data processing. Analysts have long argued that the economic viability of such systems depends on continued reductions in launch costs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starmind_(satellite)">Starmind (satellite) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Orbital_data_centers">Orbital data centers</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/another-star-is-born-spacex-names-ai-megaconstellation-starmind">Another 'Star' is born: SpaceX names AI megaconstellation ...</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#AI infrastructure`, `#satellites`, `#orbital data centers`, `#regulation`

---

<a id="item-7"></a>
## [Ubuntu's Slow Security Patches Spark Debian Migration Debate](https://www.openwall.com/lists/oss-security/2026/11/25/9) ⭐️ 7.0/10

A post on the oss-security mailing list, discussed on Hacker News, highlights complaints that Ubuntu is slow to ship security fixes, with commenters saying they have moved server images to Debian because of it. Ubuntu is one of the most widely deployed Linux distributions for servers and cloud VMs, so slow patching leaves operators exposed to known vulnerabilities for longer and can erode trust in its enterprise-ready positioning. The discussion includes a quoted stable-kernel maintainer arguing that systems must take all stable/LTS releases rather than cherry-picking patches, while another commenter defends slower distros by pointing to regression-testing tradeoffs and a concrete Debian QA bug; one user also notes that fixes have appeared in Ubuntu's -updates repository hours before the security repository. The thread does not present official Ubuntu response-time data.

hackernews · gslin · Nov 25, 20:38 · [Discussion](https://news.ycombinator.com/item?id=50647181)

**Background**: Ubuntu is a Debian-derived Linux distribution maintained by Canonical, and it is commonly used as a default OS for servers, cloud images, and generic virtual machines. Like other distributions, Ubuntu backports security fixes to supported releases instead of forcing full version upgrades, and it publishes those fixes through separate security and updates repositories. Distributions must balance speed of patching against the risk that a rushed change causes regressions, which is why release and QA policies vary widely.

**Discussion**: Commenters are largely critical of Ubuntu: one reports moving all server images to Debian, and another says they recently chose Debian for a generic VM after hesitating over slow patches. Others push back by emphasizing regression-testing costs and Debian's own QA limitations, while one user warns that security fixes sometimes land in Ubuntu's -updates repository before the security repository.

**Tags**: `#linux`, `#security`, `#ubuntu`, `#debian`, `#distributions`

---

<a id="item-8"></a>
## [NFS2ROOT: 12-year-old pre-auth root bug in Linux kernel NFS server](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 7.0/10

OpenSec published details of CVE-2026-99362, dubbed "NFS2ROOT," a heap overflow in the Linux kernel's NFSv4.1 server (nfsd) that lets an unauthenticated client on tcp/2049 corrupt kernel memory, carrying a reported CVSS score of 9.8. The flaw has reportedly existed since Linux 3.16 — roughly 12 years — but was already fixed upstream months before the write-up appeared. A pre-auth remote root flaw in the kernel is severe in principle, since a single network connection could compromise an entire host without credentials. In practice the impact is bounded: NFS is rarely exposed to the public internet, the fix has long been upstream, and no public proof-of-concept has been released, so the news is more a reminder about kernel attack surface than an imminent emergency. The bug is a heap overflow in the NFSv4.1 server path, triggerable by an unauthenticated client over tcp/2049, which is the standard NFS port. Commenters noted that no exploit code was posted alongside the advisory, and the practical remediation is simply updating to a kernel that already contains the upstream patch.

hackernews · dm · Nov 25, 20:35 · [Discussion](https://news.ycombinator.com/item?id=50647161)

**Background**: NFS (Network File System) is a distributed file system protocol originally developed by Sun Microsystems in 1984 that lets a client mount and use files on a remote server as if they were local. On Linux, the server side is implemented in-kernel by the nfsd component, so a memory-safety bug there runs with full kernel privileges. "Pre-auth" means the flaw can be hit before any authentication or credential exchange takes place, and CVSS 9.8 is the "critical" band of the common vulnerability scoring scale.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baeldung.com/cs/nfs">What Is a Network File System ? | Baeldung on Computer Science</a></li>
<li><a href="https://wiki.archlinux.org/title/NFS">NFS - ArchWiki</a></li>

</ul>
</details>

**Discussion**: Reaction was measured rather than alarmed: one commenter shared a specific rule for the "yeet" XDP-based L7 programmable firewall that he says mitigates the issue and confirmed in CI, while others pointed out that no PoC has been published and that the bug was patched upstream months ago. Several readers argued NFS was never considered safe to expose to the public internet anyway, with one using the bug as an argument that C code should not face the internet and another holding it up as a reminder that seL4 exists and Linux's trusted computing base keeps growing.

**Tags**: `#Linux kernel`, `#NFS`, `#security vulnerability`, `#remote exploit`, `#CVE`

---

<a id="item-9"></a>
## [Developer reverse-engineers Windows loudness equalization and ports it to PipeWire](https://github.com/xoxorwr/pw-loudness-eq) ⭐️ 7.0/10

A developer publishing under the handle xoxorwr released pw-loudness-eq on GitHub, a PipeWire audio filter that reproduces the loudness equalization and limiting behavior found in Windows. The implementation was derived by reverse-engineering Windows' audio engine, specifically the CAudioLimiter component in AudioEng.dll that runs inside the audiodg.exe audio device graph process. Linux users who miss the volume-leveling behavior of Windows — where quiet dialogue and loud explosions end up at similar levels — can now get an equivalent effect natively in PipeWire. The project also draws attention to the fact that Windows silently compresses audio in shared mode, a detail that matters to anyone capturing, measuring, or comparing audio output on Windows. According to commenters, the Windows processing only applies to shared-mode paths such as WASAPI shared, DirectSound and MME, and not to WASAPI exclusive mode or ASIO, with the compression being very subtle at roughly -0.1 dB on peaks. Critics note the algorithm is really loudness normalization followed by a limiter rather than frequency-dependent equalization, and that it can be prone to boosting focused impulses such as whistles or pure tones, which is why a limiter stage is needed at the end.

hackernews · ThrowNotAway · Nov 25, 11:34 · [Discussion](https://news.ycombinator.com/item?id=50641171)

**Background**: Windows has long offered a "Loudness Equalization" enhancement in the Sound control panel that brings very loud and very quiet content closer to an average level, which is useful for movies or games with wide dynamic range. PipeWire is the modern Linux audio and video server that replaces PulseAudio and JACK, and it supports filter chains that can insert custom DSP into the audio graph. On Windows, WASAPI shared mode mixes all applications through the system audio engine, while exclusive mode and ASIO let an application talk to the hardware directly — which is why the hidden processing only shows up in the shared path.

<details><summary>References</summary>
<ul>
<li><a href="https://pipewire.org/">PipeWire</a></li>
<li><a href="https://en.wikipedia.org/wiki/Audio_normalization">Audio normalization - Wikipedia</a></li>
<li><a href="https://www.thewindowsclub.com/disable-or-enable-loudness-equalization-in-windows-10">How to disable or enable Loudness Equalization in Windows 11/10</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread mixed technical insight with skepticism: one commenter detailed how Windows' hidden limiter works in shared-mode WASAPI, DirectSound and MME but not exclusive mode or ASIO, while another insisted the feature is loudness normalization, not equalization, and warned it can boost pure tones. Others questioned why reverse-engineering a Windows DLL was necessary at all, calling the algorithm simple to implement and the approach potentially unethical, and one commenter objected that flattening dynamics defeats the purpose of a composition's dynamic range.

**Tags**: `#audio`, `#PipeWire`, `#reverse-engineering`, `#Windows`, `#loudness-normalization`

---

<a id="item-10"></a>
## [Blogger Audits Clojure's Core Library with Lean, Reports Unreported Bugs](https://s.conao3.com/blog/2026/e4f733) ⭐️ 7.0/10

A developer used the Lean theorem prover to formally check Clojure's core library (clojure.core) and published a list of bugs that had not previously been reported upstream. The post, titled "I checked Clojure's core with Lean and found unreported bugs," triggered a substantial Hacker News discussion about whether such findings are genuine defects or artifacts of modeling. Clojure underpins production systems at companies such as Nubank, so defects in clojure.core ripple across a large ecosystem of JVM applications. The experiment also shows how proof assistants like Lean are moving from academic exercises into practical auditing of widely used libraries, complementing traditional testing and static analysis. Commenters pushed back on the bug list: one noted that (.indexOf (seq (byte-array [1 2 3])) 2) fails only because a Clojure literal like 2 is a Long that does not match the byte type the array expects, and that (get "abc" 1.9) fails because get coerces keys to integers in the context of strings — both arguably expected behavior rather than bugs. The main open question is how to separate real defects from modeling noise when translating idiomatic Clojure semantics into Lean.

hackernews · encyclopedism · Nov 25, 14:56 · [Discussion](https://news.ycombinator.com/item?id=50642939)

**Background**: Lean is a proof assistant and functional programming language based on dependent type theory, developed since 2013 and now maintained with support from the nonprofit Lean Focused Research Organization; it is used to write machine-checked proofs about programs. Clojure's core library is the fundamental standard library of the Clojure language, providing the primitive data types and functions that nearly all Clojure code relies on. Formal verification means proving or disproving a system's correctness against a formal specification using mathematical methods, while static analysis examines programs without executing them; both differ from ordinary unit testing, which only samples behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Static_program_analysis">Static program analysis - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread was skeptical but engaged: one commenter identified two entries in the list that look like type-coercion misunderstandings and argued such audits need to cut noise to be useful, while another questioned whether Lean is now displacing Rocq (formerly Coq) for this kind of work and whether language models simply write Lean better. Others pointed to the scale of the problem — one reader said they found dozens of issues in SBCL, Clozure CL, and ACL2 in a similar audit — and one commenter noted that Nubank, a major Clojure user, would expect such core primitives to be spotless.

**Tags**: `#Clojure`, `#Lean`, `#formal verification`, `#static analysis`, `#programming languages`

---

<a id="item-11"></a>
## [New York Times Warns Photographers Against Updating Photoshop Over AI Features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features) ⭐️ 6.0/10

The New York Times has issued a warning to photographers it works with, advising them not to update Photoshop because of the AI features baked into newer versions. The guidance, reported by The Verge, reflects the paper's concern that AI-driven editing tools could tag or taint images it publishes. A major publisher publicly steering contributors away from a flagship creative tool shows how AI provenance concerns are now shaping real editorial workflows, not just policy debates. If other outlets follow, Adobe could face pressure to offer AI-free or verifiable editing modes, and photographers may migrate to alternatives. The core problem is that AI edits and fully generated images are hard to distinguish once the output is a flat image file, and platforms may attach automatic "AI-generated" labels based on embedded provenance metadata. Notably, even minor AI-assisted operations such as color tweaks, cutouts, or layout adjustments can trigger the same labeling, which complicates the Times' blanket advice.

hackernews · rmason · Nov 25, 21:18 · [Discussion](https://news.ycombinator.com/item?id=50647673)

**Background**: Modern Adobe tools such as Firefly-powered Generative Fill embed Content Credentials, a cryptographically signed metadata standard developed by the Coalition for Content Provenance and Authenticity (C2PA) that records how an asset was created and edited. Platforms including Meta have begun reading these signals to label images as AI-generated. Because the labels are attached to the file rather than the intent, a photojournalist who makes one AI-assisted tweak can end up with an image that looks machine-made to viewers and algorithms alike.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Content_Credentials">Content Credentials - Wikipedia</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>
<li><a href="https://www.adobe.com/products/firefly.html">Adobe Firefly - Free Generative AI for Creatives</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed the stigma is real: one creative-tools practitioner said it is nearly impossible to separate a fully generated image from one with a minor AI edit, and that an "AI generated content" tag on Instagram or Facebook is a credibility "death blow" for brands. Others saw an opening for competitors such as Affinity and noted at least one European press agency already moving away from Photoshop, while some framed it as part of a broader backlash against subscriptions and US software.

**Tags**: `#AI ethics`, `#Photoshop`, `#content provenance`, `#creative tools`, `#publishing`

---

<a id="item-12"></a>
## [Hobbyist runs tiny Qwen LLM on bare metal in pure assembly, no OS](https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os) ⭐️ 6.0/10

A hobbyist project published on GitHub (alesha-pro/llm.asm, under 02-baremetal-os) runs a small Qwen language model directly on bare metal in hand-written assembly, with no operating system and no syscalls. The repository's top-level README benchmarks this bare-metal build against a pure-assembly Linux ELF version of the same code and against llama.cpp. It is a striking demonstration of how far minimal-dependency inference can be pushed, showing that a transformer model can execute with only firmware-level support rather than a full OS stack. While it has little immediate practical value, it illustrates the lower bound of the software stack needed for LLM inference and offers a reference point for anyone interested in embedded or highly constrained deployment. The model involved is a very small Qwen variant, so absolute performance numbers are modest and the comparison is as much about the harness as the model. Running without syscalls removes an entire class of attack surface, but it also means no filesystem, networking, or standard I/O, so the model has no way to interact with anything beyond whatever the firmware and the code itself provide.

hackernews · miohtama · Nov 25, 22:15 · [Discussion](https://news.ycombinator.com/item?id=50648365)

**Background**: Bare-metal programming means writing software that runs directly on the hardware with no operating system underneath — common in embedded systems and bootloaders, where the program supplies its own startup code and device drivers. Qwen is Alibaba Cloud's family of open-weights language models, whose smaller releases are widely used as starting points for local and experimental work. llama.cpp is an open-source C/C++ inference library built on the GGML tensor library, and it has become the de facto baseline for local LLM inference, powering tools like Ollama and LM Studio.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bare_machine">Bare machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>

</ul>
</details>

**Discussion**: Commenters found the concept genuinely cool and compared it to the self-booting disks of the past, but most were skeptical of its utility: one likened it to Futurama's "brain in a jar" — a lot of work with little real-world application — and another asked whether such a small model is useful without a harness to interact with. A security-minded commenter noted that omitting syscalls is one way to eliminate an attack vector, while also wondering which processor mode the code runs in.

**Tags**: `#llm`, `#bare-metal`, `#assembly`, `#qwen`, `#systems-programming`

---

<a id="item-13"></a>
## [Blogger Claims TypeSafe's 'Jev' Is Actually Qwen3.5-35B-A3B](https://modaic.dev/blog/latency-doesnt-lie) ⭐️ 6.0/10

A Modaic blog post titled "Latency Doesn't Lie" argues that TypeSafe's model product "Jev" is most likely a re-served version of Alibaba's open-weight Qwen3.5-35B-A3B, citing measured API latency profiles and the model's self-identification responses as evidence. The claim is speculative rather than proven, and the post drew a 212-point Hacker News thread with 59 largely skeptical comments. The episode highlights a growing practice of "model fingerprinting"—trying to determine which underlying LLM a closed API actually serves—which matters for buyers assessing whether a vendor's claimed proprietary model is genuinely novel or a thin wrapper over open weights. It also raises uncomfortable questions about disclosure norms and the credibility of investigations published by direct competitors. The core weakness is methodological: commenters point out that the author's own latency data does not separate Qwen from Gemma, and that self-identification prompts have been known to be unreliable since the earliest ChatGPT days; the post also reportedly omits self-identification experiments run against other candidate models. TypeSafe's own website explicitly states that "Jev is neither small nor an LLM," directly contradicting the premise, and Modaic is a competitor to TypeSafe, creating a conflict of interest absent independent reproduction.

hackernews · csoham · Nov 25, 22:57 · [Discussion](https://news.ycombinator.com/item?id=50648823)

**Background**: LLM fingerprinting is the practice of inferring which model sits behind an API from behavioral signals rather than metadata—using techniques such as latency and throughput profiling, tokenizer artifacts, refusal patterns, and carefully crafted probe prompts. It is inherently probabilistic, since providers can add caching, routing, quantization, and system prompts that blur the underlying model's signature. Qwen3.5-35B-A3B is Alibaba's open-weight image-text-to-text model with roughly 36B total parameters and, as the "A3B" suffix indicates, about 3B active parameters per token in a mixture-of-experts design, which makes it cheap and fast to serve—consistent with the latency argument in the post.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/llm-fingerprinting">LLM Fingerprinting Techniques - emergentmind.com</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-35B-A3B">Qwen/Qwen3.5-35B-A3B · Hugging Face</a></li>
<li><a href="https://ollama.com/library/qwen3.5:35b-a3b">qwen3.5:35b-a3b</a></li>

</ul>
</details>

**Discussion**: Sentiment in the Hacker News thread is broadly skeptical. Commenters argue that the presented latency data cannot distinguish Qwen from Gemma, note that the self-identification experiments were not run against other candidate models, point to TypeSafe's website explicitly denying Jev is an LLM, and flag that Modaic is a competitor to TypeSafe so the results need independent reproduction before being taken seriously.

**Tags**: `#LLM fingerprinting`, `#model identification`, `#Qwen`, `#API reverse engineering`, `#HN discussion`

---

<a id="item-14"></a>
## [US stocks slide as AI fears intensify, Nasdaq drops nearly 4%](https://www.bbc.co.uk/news/articles/cq0md8g14zryo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

All three major US stock indexes fell in early trading, with the tech-heavy Nasdaq down almost 4% as concerns about artificial intelligence intensified. The decline marks a broad sell-off rather than one confined to a single sector or company. The Nasdaq's sharp move shows how sensitive the current market rally is to AI sentiment, since a handful of large AI-linked companies carry outsized weight in US indexes. A sustained pullback could affect the cost of capital for AI-focused startups and reshape investor appetite across the tech sector. The report is an early-trading snapshot rather than a closing figure, so the final scale of the losses could differ, and it does not specify which individual stocks or news items drove the sell-off. It also gives no indication of whether the decline reflects a single catalyst or a broader reassessment of AI valuations.

rss · BBC Business · Nov 25, 21:43

**Background**: The Nasdaq Composite is a US stock index heavily weighted toward technology companies, which makes it a common proxy for sentiment toward the tech industry. In recent years, enthusiasm around artificial intelligence has driven large gains in a relatively small group of chipmakers, cloud providers and software firms, concentrating index performance in AI-exposed names. Because of that concentration, shifts in AI sentiment can move the whole index sharply, and a broad decline spanning all three main US indexes signals caution reaching beyond tech alone.

**Tags**: `#AI`, `#stock market`, `#tech industry`, `#Nasdaq`, `#market sentiment`

---

<a id="item-15"></a>
## [Hera images reveal stadium-sized crater from NASA's DART asteroid impact](https://www.bbc.co.uk/news/articles/cw8dv112r5gmo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

New close-up images from the European Space Agency's Hera spacecraft show the asteroid Dimorphos with a crater roughly the size of a stadium, gouged out when NASA's DART probe deliberately slammed into it four years ago. The images offer the first detailed look at how the 160-metre-wide moonlet's surface and shape were reshaped by the 2022 kinetic impact. The findings turn the DART demonstration from a one-off orbital deflection measurement into a fuller picture of what an asteroid actually does when hit, which is essential if kinetic impactors are ever to be used to protect Earth from a real threat. They also show how much of the deflection came from debris recoil rather than the spacecraft's own momentum, a key factor in planning future planetary-defense missions. DART struck Dimorphos at about 23,000 km/h on 26 September 2022, shortening its orbit around the larger asteroid Didymos by roughly 32 minutes — well beyond the 73-second threshold set as mission success. The impact's momentum transfer was amplified by ejected debris, and the crater's scale suggests Dimorphos may be a loosely bound rubble pile rather than a solid body, which affects how such asteroids respond to impacts.

rss · BBC World · Nov 25, 17:30

**Background**: DART (Double Asteroid Redirection Test) was NASA's first planetary-defense mission, a joint project with the Johns Hopkins University Applied Physics Laboratory, designed to test the "kinetic impactor" technique: hitting a harmless asteroid head-on to see whether its path could be nudged. Dimorphos is a small moonlet orbiting the asteroid Didymos; neither poses any threat to Earth, which made the pair an ideal and safe test target about 11 million kilometres away. NASA measured the deflection from afar, but the European Space Agency's Hera spacecraft was sent to inspect the aftermath up close, arriving years later to map the crater, mass and internal structure of the asteroid.

<details><summary>References</summary>
<ul>
<li><a href="https://www.esa.int/articles/about-us/directorates/operations/space-safety/hera/hera-reveals-stadium-sized-asteroid-crater-left-after-spacecraft-impact">Hera reveals stadium-sized asteroid crater from spacecraft impact</a></li>
<li><a href="https://edition.cnn.com/2026/11/25/science/hera-mission-dimorphos-asteroid-arrival-images">ESA mission reveals stadium-size crater left by first planetary defense ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Double_Asteroid_Redirection_Test_(DART)">Double Asteroid Redirection Test (DART)</a></li>

</ul>
</details>

**Tags**: `#planetary defense`, `#asteroid`, `#DART mission`, `#space science`, `#NASA`

---

<a id="item-16"></a>
## [Huawei guilty of stealing US trade secrets, acquitted of racketeering](https://www.bbc.co.uk/news/articles/cmy49ngydqzpo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

A federal jury in New York found Huawei guilty of stealing US trade secrets, but acquitted the company of racketeering charges following a months-long trial. The mixed verdict means the Chinese telecom giant is convicted on the trade-secret counts while avoiding the broader, more severe racketeering conspiracy allegations. The conviction marks a rare criminal judgment against a major Chinese technology company in a US court, adding a new legal precedent to the already tense US-China tech relationship. It could complicate Huawei's remaining business dealings and negotiations in the US, and signals that trade-secret prosecutions against foreign firms remain an active enforcement priority for US authorities. The verdict is split: the jury convicted on the trade-secret theft counts while clearing the company of racketeering, a charge that would have implied a broader pattern of criminal enterprise. Sentencing and any appeal are expected to follow, and the case does not in itself resolve Huawei's separate status under US export and procurement restrictions.

rss · BBC World · Nov 25, 10:52

**Background**: Trade-secret theft under US law refers to obtaining a company's confidential proprietary information — such as source code, designs or manufacturing know-how — without authorization, and it can be prosecuted both civilly and criminally. Racketeering, rooted in the RICO statute originally aimed at organized crime, is a much heavier charge that requires proving a pattern of illegal activity carried out as an enterprise. Huawei is a major Chinese telecommunications equipment and device maker that has been at the center of US-China technology tensions for years, so any US criminal proceeding involving the company carries outsized geopolitical weight.

**Tags**: `#Huawei`, `#trade secrets`, `#US-China relations`, `#technology industry`, `#legal`

---

<a id="item-17"></a>
## [BBC Analysis: Jensen Huang Has Made Himself Irreplaceable at Nvidia](https://www.bbc.co.uk/news/articles/c3rrgqj2zx5yo?at_medium=RSS&at_campaign=rss) ⭐️ 5.0/10

The BBC published a commentary piece by its technology and AI editor, Zoe Kleinman, arguing that Nvidia CEO Jensen Huang has made himself effectively impossible to fire. The article examines how Huang's personal leadership has become tightly bound up with the company's identity and success. Nvidia sits at the center of the global AI boom as the dominant supplier of the GPUs used to train and run large models, so questions about its leadership and succession carry weight well beyond the company itself. The piece also touches a broader governance theme: how founder-CEOs can accumulate influence that makes ordinary board oversight largely theoretical. This is a short opinion and analysis column rather than a technical deep-dive or a report of a new announcement, and it centers on Huang's personal standing rather than on products, financials or roadmap details. Readers looking for concrete news about Nvidia's hardware or business results will not find it here.

rss · BBC Business · Nov 25, 10:03

**Background**: Nvidia designs the graphics processing units (GPUs) that turned out to be exceptionally well suited to the parallel computation behind modern AI, which made the company a central supplier to the AI industry. Jensen Huang co-founded Nvidia and has served as its CEO since the early 1990s, an unusually long tenure that has made him one of the most prominent figures in technology. The AI boom has sharply raised Nvidia's prominence and valuation, intensifying interest in how much of that success is attributable to its leader.

**Tags**: `#Nvidia`, `#Jensen Huang`, `#AI industry`, `#leadership`, `#corporate governance`

---

<a id="item-18"></a>
## ['Paris Manifesto' Open Letter Urges Democracies to Counter AI-Era Extreme Wealth](https://www.theguardian.com/commentisfree/2026/nov/25/paris-manifesto-open-letter-ai-oligarchy) ⭐️ 5.0/10

A Guardian open letter published on November 25, 2026 — billed as a "Paris manifesto" — argues that democracy can still reverse the slide into oligarchy, but only if governments act now. It cites the ballooning fortunes of the world's roughly 3,000 richest households, whose combined wealth has grown from 3% of global GDP when Forbes began its rankings in 1987 to 17% today. The letter links two trends that are usually discussed separately — runaway wealth concentration and the rise of AI — arguing that AI's capital-intensive economics could lock in a small elite's hold on economic and political power. If that framing gains traction, it could push AI regulation debates beyond safety and competition toward tax policy, antitrust and campaign-finance reform. The piece is an opinion/open letter rather than a technical or empirical study, and the excerpt offers no specific policy instruments, thresholds or enforcement mechanisms — only the claim that the oligarchy dynamic is reversible. The headline statistic is drawn from Forbes' billionaires rankings dating back to 1987, a source that measures disclosed fortunes rather than underlying control of capital.

rss · The Guardian Business · Nov 25, 11:00

**Background**: An oligarchy, from the Greek for "rule by few," is a system in which power rests with a small group — in this debate, a handful of ultra-wealthy tech founders and investors. Scholars and policy institutes have spent the past few years studying a "tech oligarchy," the concentration of AI capability, compute and data among a small number of firms and individuals, and what that means for democratic governance. Because frontier AI requires enormous capital expenditure on data centers and chips, critics argue it naturally funnels both money and influence toward whoever already holds the most of both.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oligarchy">Oligarchy - Wikipedia</a></li>
<li><a href="https://www.hks.harvard.edu/faculty-research/policy-topics/science-technology-data/what-does-tech-oligarchy-look">What does a tech oligarchy look like? | Harvard Kennedy School</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#wealth inequality`, `#democracy`, `#tech policy`, `#oligarchy`

---

<a id="item-19"></a>
## [University of Sydney makes oral defence mandatory for all honours theses to counter AI](https://www.theguardian.com/australia-news/2026/nov/25/australian-universities-tackle-ai-plagiarism-oral-assessment-honours-masters-phd) ⭐️ 5.0/10

The University of Sydney now requires every student in its one-year honours program to defend their roughly 20,000-word thesis in a spoken conversation with professors, rather than relying on the written submission alone. The Guardian reports that honours students across Australia are increasingly being asked to sit oral assessments, with Sydney's blanket requirement among the most sweeping. Generative AI has made written coursework a weak signal of whether a student actually understands or produced the work, so assessment is shifting toward formats that are hard to outsource. If oral defence becomes standard at honours and postgraduate level, it could reshape how degrees certify authorial competence and spread to other institutions and disciplines. Oral examinations — often called viva voce or simply a viva — are long established for PhD and masters-by-research degrees, but are unusual as a mandatory requirement for every honours cohort because they are staff-intensive and hard to scale. The article centres on student Aidan Elwig Pollock, who did not expect a spoken component alongside his 20,000-word thesis, and it offers little detail on grading weight or examiner procedure.

rss · The Guardian World · Nov 25, 14:00

**Background**: A viva voce is an oral examination in which students defend their thesis and answer examiners' questions, traditionally used at PhD level to confirm the work is genuinely the candidate's own and that they understand it. Plagiarism detection tools were built for comparing text against known sources, and they perform poorly on LLM-generated prose, which is original in wording even when no real research was done. Universities have therefore begun experimenting with 'AI-resistant' assessment design, including in-person verbal components, handwritten exams and tasks tied to local or personal context.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cambridgestudents.cam.ac.uk/your-course/research-students-pgr/postgraduate-exam-information/writing-submitting-and-examination/phd/oral-examination">The oral examination (viva) | Cambridge students</a></li>
<li><a href="https://en.wikipedia.org/wiki/Viva_voce">Viva voce - Wikipedia</a></li>
<li><a href="https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1499495/full">AI-resistant assessments in higher education ... - Frontiers</a></li>

</ul>
</details>

**Tags**: `#AI in education`, `#academic integrity`, `#LLM plagiarism`, `#assessment design`, `#higher education policy`

---

