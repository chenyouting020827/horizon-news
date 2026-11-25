---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 133 items, 15 important content pieces were selected

---

1. [Ternary Bonsai 2.5 27B shows compressed local coding models are catching up](#item-1) ⭐️ 8.0/10
2. [OpenAI says GPT-6.2 designs proteins from scratch by writing code](#item-2) ⭐️ 8.0/10
3. [GreyNoise tracks active campaign hacking Check Point security management servers](#item-3) ⭐️ 8.0/10
4. [GTA 6's Leaked Xbox Build Runs on Windows via Wine-Style Recompilation](#item-4) ⭐️ 8.0/10
5. [Quad9 Deactivates Its Public DNS Service in France Over Legal Constraints](#item-5) ⭐️ 8.0/10
6. [Helsinki's Gödel Enigma Project Deciphers Gödel's Shorthand Notebooks](#item-6) ⭐️ 7.0/10
7. [Porting a Cayley Graph Solver from CUDA to JAX to TorchTPU](#item-7) ⭐️ 7.0/10
8. [Versine launches MCP wallet so AI agents can send and request money](#item-8) ⭐️ 6.0/10
9. [songe: a training engine that improves your local LLM using idle compute](#item-9) ⭐️ 6.0/10
10. [Trump's Nvidia Intervention Ties His Political Fate to the AI Boom](#item-10) ⭐️ 6.0/10
11. [Heart Attack and Stroke Risk Can Be Predicted Decades in Advance](#item-11) ⭐️ 5.0/10
12. [Jetty Pro, a New Mac Dock Alternative, Sparks Subscription Pricing Debate](#item-12) ⭐️ 5.0/10
13. [Tech sell-off resumes as Nvidia rally fades after Huang's return](#item-13) ⭐️ 5.0/10
14. [EU to Cap Chinese Hybrid Vehicle Imports With Temporary Quotas](#item-14) ⭐️ 5.0/10
15. [Victoria election could decide fate of nine datacentre projects](#item-15) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Ternary Bonsai 2.5 27B shows compressed local coding models are catching up](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

PrismML released Ternary Bonsai 2.5 27B, a ternary-quantized small language model that community testers report running locally at roughly 22–25 tokens/s on Apple Silicon while scoring competitively on SWE-bench Verified. One user measured 22.3 tokens/s generation on a Mac Mini M5 Pro with 24GB RAM and said 128k context fits easily in memory. This suggests aggressive ternary compression can shrink a 27B model to consumer-hardware size without collapsing coding ability, potentially making local agentic coding workflows practical on laptops and small desktops. If the trend holds, frontier-like coding performance could become accessible on 24–32GB machines rather than datacenter GPUs. Ternary quantization stores each weight as -1, 0 or +1 plus a small per-group scale factor, cutting model size roughly sevenfold; the 27B release is reported at about 5.9 GB and roughly 1.76 bits per weight, runnable on 8GB-VRAM GPUs or Apple Silicon. Caveats include concerns about benchmark overfitting and the lack of native hardware acceleration for ternary weights outside FPGAs.

hackernews · b0m · Nov 24, 20:08 · [Discussion](https://news.ycombinator.com/item?id=50633922)

**Background**: Ternary quantization is a post-training compression technique that replaces 16-bit weights with three values (-1, 0, +1) plus small scale factors, greatly reducing storage and memory needs. SWE-bench is a benchmark that evaluates models on real software-engineering tasks, and SWE-bench Verified is a curated subset commonly used for coding-model comparisons. Small language models generally refer to models in the billions of parameters, designed to run on limited hardware; ternary quantization is one way to make them fit local devices.

<details><summary>References</summary>
<ul>
<li><a href="https://eyestech.in/prismml-ternary-bonsai-2-27b-quantization-deep-dive/">PrismML Ternary Bonsai 2 27B: 5.9GB & 143 Tok/Sec</a></li>
<li><a href="https://www.mindstudio.ai/blog/ternary-bonsai-2-9b-gguf-local">Ternary Bonsai 2 9B GGUF: Run a 2.4GB Vision Model... | MindStudio</a></li>
<li><a href="https://www.swebench.com/">SWE-bench Leaderboards</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive: users report 22–25 tokens/s on a Mac Mini M5 Pro with 24GB RAM, 128k context fitting in memory, and a decent Pelican test from a 1-bit-style model using 7–8GB RAM on an M3 MacBook Air. Some commenters are optimistic about 24–32GB laptops eventually running Opus 4.6-level models, while skeptics question whether SWE-bench gains reflect “benchmaxxing,” request direct comparisons with equivalent Q1/Q2 quantized models, and ask about hardware acceleration for ternary weights beyond FPGAs.

**Tags**: `#ternary quantization`, `#small language models`, `#local inference`, `#SWE-bench`, `#model compression`

---

<a id="item-2"></a>
## [OpenAI says GPT-6.2 designs proteins from scratch by writing code](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10

OpenAI published a report stating that its GPT‑6 family, specifically GPT‑6.2, can design de novo minibinders when given the 3D structures of five target proteins with the desired attachment sites marked, generating three-dimensional designs by writing its own code rather than calling specialized protein AI models. An internal research model reportedly matched or outperformed specialized protein design models on many tasks. If a general-purpose language model can carry out core protein design steps through code generation alone, it could lower the barrier to computational biology work that has until now required a stack of task-specific models such as structure generators and sequence-design tools. The claim also sharpens the debate over whether frontier LLMs are becoming genuine scientific instruments or are mostly orchestrating the specialized tools built by protein-design labs. The workflow was hybrid: GPT‑6.2 produced the 3D backbones, but a specialized model called SolubleMPNN suggested amino acid sequences for each design, and other specialized protein models helped filter candidates predicted to fold as intended and bind at the correct site before lab testing. The described setup involved only five target proteins, and the lab validation was handled by specialized models, so the results do not yet show end-to-end protein design by the LLM alone.

hackernews · acossta · Nov 24, 21:02 · [Discussion](https://news.ycombinator.com/item?id=50634658)

**Background**: De novo protein design means creating proteins that do not exist in nature, and a minibinder is a small designed protein that sticks tightly to a chosen site on a target protein, an approach explored as a compact alternative to antibodies. The design problem has two halves: generating a three-dimensional backbone geometry, and finding an amino acid sequence that folds into that geometry and binds where intended — the second half is often called inverse folding and is normally handled by dedicated models. Recent progress in this field has come from specialized deep-learning systems trained on protein structure data, which is why OpenAI's claim that a general model can handle parts of the job without them is notable.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT-6 models demonstrate intrinsic protein-design ... - OpenAI</a></li>
<li><a href="https://www.nature.com/articles/s44222-025-00349-8">AI-driven protein design - Nature Reviews Bioengineering</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were split: a Baker lab PhD alum said the direction makes sense and that fusing language models with protein modeling was laughed at five years ago but is now the likely future, while others asked what GPT‑6.2 actually designed given that SolubleMPNN supplied the sequences — noting that for proteins the sequence essentially determines the structure. The thread's dominant sentiment was interest tempered by skepticism about how much of the result reflects the LLM versus the specialized tools wrapped around it.

**Tags**: `#protein design`, `#LLMs`, `#AI for science`, `#OpenAI`, `#computational biology`

---

<a id="item-3"></a>
## [GreyNoise tracks active campaign hacking Check Point security management servers](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 8.0/10

GreyNoise published a detailed writeup of an ongoing intrusion campaign against Check Point Security Management Servers that begins with exploitation of CVE-2026-16232, a SmartConsole authentication bypass, using a script adapted from a public Metasploit module. In one intrusion, the actor pivoted to an HFS server and collected repeated session cookies from the loginSrp1 endpoint to reconstruct the Node.js V8 PRNG internal state, recovering the cookie-signing key and forging an admin session cookie. The campaign shows real-world attackers chaining an authentication-bypass flaw in a core security-management product with a subtle cryptographic weakness to gain full administrative control, meaning organizations whose management servers are internet-exposed may already be compromised. The PRNG technique is notable because it turns a well-known but widely ignored misuse of Math.random() into a practical session-forgery exploit. V8 implements Math.random() with the non-cryptographic xorshift128+ PRNG, so enough consecutive outputs allow an attacker to rebuild its internal state and then rewind it to server startup to reproduce the randomId(30) call that generated the cookie-signing key. With a forged admin cookie the actor can reach administrative functions such as the server_code configuration feature, which allows server-side JavaScript execution.

hackernews · louiereederson · Nov 24, 16:32 · [Discussion](https://news.ycombinator.com/item?id=50630594)

**Background**: Check Point Security Management Servers are the central console used to configure and monitor Check Point firewalls and security policies, so administrative control over them is equivalent to control over the whole security estate. JavaScript's Math.random() is a pseudo-random number generator: its output is entirely determined by an internal state, and it is explicitly not designed for security purposes such as generating keys or session tokens. If an application draws secrets from Math.random(), anyone who observes enough outputs can predict every past and future value, which is exactly what happened here.

<details><summary>References</summary>
<ul>
<li><a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign">An Active Intrusion Campaign Against Check Point Security ...</a></li>
<li><a href="https://v8.dev/blog/math-random">There’s Math. random (), and then there’s Math. random () · V 8</a></li>
<li><a href="https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html">Attackers Target Rejetto HFS Flaw That Enables Admin Session ...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed a mix of weary recognition and alarm, with several joking about the perennial return of PRNG weaknesses while one argued that Math.random() itself should be hardened rather than blaming the hundreds of applications that misuse it. Others warned that LLM-driven attackers will soon make such campaigns routine, and one commenter questioned how initial access was obtained, noting the link between multiple victims suggests CVE-2026-16232 and asking whether all of them really exposed their management servers to the internet.

**Tags**: `#security`, `#vulnerability-exploitation`, `#PRNG`, `#Check Point`, `#incident-response`

---

<a id="item-4"></a>
## [GTA 6's Leaked Xbox Build Runs on Windows via Wine-Style Recompilation](https://twitter.com/raul_bs3/status/2125213756238291075) ⭐️ 8.0/10

A Hacker News thread highlighted community efforts to get the leaked Xbox build of GTA 6 running on Windows PCs using Wine-like recompilation projects, chiefly the efforts referred to as xcl and Victory. According to commenters, the game's actual console code now boots and executes on PC, with the remaining work concentrated on compatibility layers and graphics rather than on getting the binary to run at all. This is a strong demonstration that the gap between a modern Xbox release and a PC build is largely a compatibility problem rather than a hard technical barrier, which weakens console exclusivity as a practical restriction. At the same time, the GitHub takedown of the related Leonida recompilation project shows that legal pressure, not engineering difficulty, may be the real limit on game preservation efforts like this. Commenters note that the leaked Xbox binary has no special DRM or obfuscation, so the hard problems are graphics translation and Xbox-specific platform compatibility, which the Wine-like projects must emulate. Comparable research projects such as Xbox2Windows explicitly label full-game startup as unverified, and the Leonida static recompilation effort was taken down from GitHub while its lead developer was in school.

hackernews · andrem · Nov 24, 13:19 · [Discussion](https://news.ycombinator.com/item?id=50627783)

**Background**: Static recompilation is a technique that translates a console game's machine code into source code (usually C) ahead of time and then compiles it natively for another platform, so no emulator runs at play time. Wine is a compatibility layer that lets Windows programs run on other operating systems by translating Windows API calls instead of emulating hardware, and the projects here take a similar approach to the Xbox build. Modern Xbox consoles run a Windows-derived OS on x86-64 hardware, so their game binaries are structurally close to standard Windows PE executables, which is why running the code is described as relatively easy.

<details><summary>References</summary>
<ul>
<li><a href="https://gta6recomp.com/leonida">Leonida — GTA 6 PC Static Recompilation Project Tracker & Source</a></li>
<li><a href="https://github.com/R0Y00/Xbox2Windows">GitHub - R0Y00/ Xbox 2Windows: Static recompilation research for...</a></li>
<li><a href="https://www.dsebastien.net/static-recompilation/">Static recompilation - dsebastien.net</a></li>

</ul>
</details>

**Discussion**: The discussion is technically enthusiastic but split on implications: one commenter explains that because modern Xbox is close to a Windows PC and the binary lacks DRM, only compatibility and graphics remain as hurdles, while another asks why a build leak was needed at all and predicts a future where games keep critical components in the cloud to prevent decompilation. Others argue the effort is not an existential threat to game production, framing it as a continuation of the usual pushback against restrictive releases and noting GTA 6's enormous budget and profitability.

**Tags**: `#game-reverse-engineering`, `#recompilation`, `#wine`, `#xbox`, `#dmca`

---

<a id="item-5"></a>
## [Quad9 Deactivates Its Public DNS Service in France Over Legal Constraints](https://quad9.net/news/blog/quad9-service-deactivation-in-france/) ⭐️ 8.0/10

Quad9 has deactivated its public DNS resolver service for users in France, with queries to 9.9.9.9 now returning a REFUSED response carrying Extended DNS Error (EDE) code 18 marked "Prohibited" and the message "Service unavailable due to French legal constraints." Community members confirmed the behavior with dig against 9.9.9.9, and a TorrentFreak report has linked the exit to an expired order in the ongoing piracy-blocking dispute. When a widely used, privacy-focused public resolver pulls out of an entire country, it shows how national legal orders can fragment the global DNS and remove a security-and-privacy option from ordinary users overnight. The case is likely to be cited in debates over DNS centralization, censorship chokepoints, and how far one country's jurisdiction can reach into foreign-operated Internet infrastructure. Quad9's withdrawal is enforced at the protocol level through EDE code 18, so affected users see an explicit legal reason rather than a silent timeout, and the service's unfiltered 9.9.9.10 endpoint and encrypted DoH/DoT transports are likewise unreachable from France. Because Quad9 is a Swiss non-profit with no reported French offices or personnel, commenters questioned whether it could simply ignore French authorities, while others set up volunteer-run caching proxies to restore access.

hackernews · farrokhi · Nov 24, 08:33 · [Discussion](https://news.ycombinator.com/item?id=50625384)

**Background**: Quad9 is a free public DNS resolver operated by a Swiss non-profit foundation whose founding charter names privacy as a primary goal, offering 9.9.9.9 and 149.112.112.112 for malware-blocking resolution, 9.9.9.10 for unfiltered resolution, and 9.9.9.11 for filtering with EDNS Client Subnet. Public resolvers sit between end users and authoritative DNS servers, which makes them a convenient chokepoint for censorship and for court-ordered domain blocking, since a single block affects everyone who uses that resolver. DoH (DNS over HTTPS) and DoT (DNS over TLS) encrypt queries to prevent tampering and eavesdropping, while Extended DNS Errors (EDE) is a standard mechanism that lets a resolver explain why a lookup failed.

<details><summary>References</summary>
<ul>
<li><a href="https://quad9.net/">Quad 9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://enterno.io/en/articles/quad9-dns">Quad 9 DNS 9.9.9.9: Addresses, Setup and Malware Blocking</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion is largely sympathetic to Quad9: one user published a volunteer-run caching/forwarding proxy (supporting DoH, DoT and Do53 over IPv4 and IPv6) as a near drop-in replacement for users in France, others verified the REFUSED/EDE 18 response with dig, and several linked two earlier high-engagement threads (1,382 and 911 points) framing the exit as a "canary in the coal mine." A recurring question was jurisdictional — since Quad9 appears to have no French offices or staff, some asked why it does not simply ignore the French authorities, while others pointed to TorrentFreak's reporting on the underlying legal dispute.

**Tags**: `#DNS`, `#privacy`, `#Internet governance`, `#censorship`, `#Quad9`

---

<a id="item-6"></a>
## [Helsinki's Gödel Enigma Project Deciphers Gödel's Shorthand Notebooks](https://www.helsinki.fi/en/researchgroups/godel-enigma/research/project-description) ⭐️ 7.0/10

The University of Helsinki's Gödel Enigma project, led by logician Jan von Plato and funded by the European Research Council from September 2018 to September 2023, is transcribing and translating Kurt Gödel's largely unstudied shorthand notebooks — including the Resultate Grundlagen and the later Arbeitshefte — with von Plato working through roughly 1,009 pages at about a page a week. Recent reports indicate that in September 2026 he fed hundreds of pages of English transcription to Claude, which surfaced 663 candidate theorems within days. Gödel is arguably the most important logician of the twentieth century, yet a large part of his private scientific output has remained effectively unread because it was written in Gabelsberger shorthand, so this project could reshape the historical understanding of mathematical logic and the foundations of computer science. The early AI-assisted results suggest that large language models may become a practical tool for unlocking other inaccessible archival corpora. The notebooks are written in Gabelsberger shorthand, a cursive German stenographic system invented around 1817, and only the 15 MaxPhil notebooks have reportedly been transcribed and studied so far — and even those remain unpublished. The project's stated aims are twofold: to build an objective picture of Gödel's role in the birth of the information society through careful source study, and to exploit his hidden discoveries using contemporary logic and formal methods.

hackernews · benbreen · Nov 24, 08:16 · [Discussion](https://news.ycombinator.com/item?id=50625265)

**Background**: Kurt Gödel (1906–1978) proved the incompleteness theorems and made foundational contributions to set theory and relativity, but he also left behind a Nachlass of notebooks, letters and unpublished manuscripts held largely at the Institute for Advanced Study. Because the scientific notebooks were kept in Gabelsberger shorthand, reading them required a rare combination of logical expertise and stenographic skill, which is why many sat untouched for decades. The Gödel Enigma project, launched at the University of Helsinki in 2017–2018, exists specifically to close that gap by producing reliable transcriptions and translations of the primary sources.

<details><summary>References</summary>
<ul>
<li><a href="https://www.helsinki.fi/en/researchgroups/godel-enigma/research/project-description">Project description | Gödel Enigma | University of Helsinki Kurt Gödel's hidden notebooks · Hacker News | Zeli ‘Ahead of his time’: AI helps unlock discoveries hidden in ... The Gödel Enigma: Unveiling a Hidden Logical Heritage Helsinki team uses Claude to surface 663 candidate theorems ... AI has decoded 1,009 pages of Kurt Gödel’s secret notebooks ...</a></li>
<li><a href="https://www.helsinki.fi/en/researchgroups/godel-enigma">Gödel Enigma | University of Helsinki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gabelsberger_shorthand">Gabelsberger shorthand</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters responded with curated reading lists — Gödel, Escher, Bach; Journey to the Edge of Reason; Gödel's Proof — and one user supplied an archived full-text link to Crocco and Engelen's 2016 volume Kurt Gödel: Philosopher-Scientist after noticing the project page's own link was broken. Others pressed on why the notebooks went unread for so long and asked for the page's publication year, while additional commenters pointed to earlier HN threads on AI-assisted Gödel work and a related logic podcast.

**Tags**: `#Gödel`, `#mathematical logic`, `#history of science`, `#archives`, `#research projects`

---

<a id="item-7"></a>
## [Porting a Cayley Graph Solver from CUDA to JAX to TorchTPU](https://andlukyane.com/blog/cayley-graphs-and-torchtpu) ⭐️ 7.0/10

A practitioner published a detailed account of porting a Cayley graph-based puzzle solver — an 88-sticker state space with 24 possible moves solved via beam search — from hand-written CUDA to JAX/XLA and then to TorchTPU, Google and Meta's PyTorch backend for TPUs. The post compares the three implementations and reports that the TPU version achieved only about 2.5% MXU tile occupancy with T=51 and head_dim=32. Most TPU performance literature focuses on dense transformer matmuls, so this account of an irregular graph-search workload exposes where XLA and the TPU's matrix units fall short when dimensions are small. It is directly useful for teams weighing PyTorch-on-TPU portability against JAX or CUDA for non-standard workloads. The core inefficiency is shape-related: TPU/XLA typically tiles arrays in 8x128 blocks to match the 32-bit vector registers, so a head dimension of 32 leaves most of the MXU tile idle. The author's conclusions come from a single algorithmic workload rather than a broad benchmark suite, so the framework trade-offs described are illustrative rather than universally applicable.

hackernews · Artgor · Nov 24, 19:40 · [Discussion](https://news.ycombinator.com/item?id=50633424)

**Background**: A Cayley graph represents a puzzle's state space as a graph where each node is a puzzle state and each edge is a legal move, turning solving into a shortest-path search; the author's solver uses beam search, which keeps only the top-k partial solutions at each step to control cost. Google's TPUs accelerate matrix math with a systolic array called the MXU, and XLA (the compiler behind both JAX and TorchTPU) partitions tensors into fixed tiles sized to that hardware. JAX compiles Python code through XLA, while TorchTPU is a newer open-source native PyTorch backend for Google Cloud TPUs developed jointly with Meta, aimed at running existing PyTorch code on TPUs with minimal changes.

<details><summary>References</summary>
<ul>
<li><a href="https://andlukyane.com/blog/cayley-graphs-and-torchtpu">From CUDA and JAX to TorchTPU: Lessons from a Cayley Graph ...</a></li>
<li><a href="https://torchtpu.readthedocs.io/">TorchTPU Documentation</a></li>
<li><a href="https://openxla.org/xla/tiled_layout">Tiled layout | OpenXLA Project</a></li>

</ul>
</details>

**Discussion**: The single comment is highly technical: one reader asks whether the author considered packing multiple puzzle states into a single MXU tile while keeping their attention computations independent, or whether XLA already exploits the batch dimension to do this automatically — pointing directly at the hardware-efficiency nuances behind the reported 2.5% occupancy figure.

**Tags**: `#cuda`, `#jax`, `#tpu`, `#performance-engineering`, `#gpu-computing`

---

<a id="item-8"></a>
## [Versine launches MCP wallet so AI agents can send and request money](https://news.ycombinator.com/item?id=50634426) ⭐️ 6.0/10

Versine, a Y Combinator (F26) startup founded by three ex-Stripe, Databricks, and Amazon engineers, launched an MCP server that sits in front of a self-custodial USDC wallet on Base, letting AI assistants in ChatGPT and Claude send and request money on a user's behalf. Payments require a passkey/biometric approval in Versine's iOS or Android app, while pre-authorized "trusted contacts" can be paid without an explicit prompt, and recipients without an account can cash out to a bank in about two minutes via claim forwarding. It is an early concrete example of "agentic payments," a space where wallets, spending limits and delegated permissions are being built specifically for AI agents rather than humans clicking buttons. If agents become the primary interface for financial tasks, whoever supplies the trusted approval and settlement layer could capture a meaningful position in consumer payments. Each agent call creates a one-time or recurring standing permission tied to a specific amount and recipient address, and users can flag trusted contacts an agent may pay without passkey approval. Choosing stablecoins over a partner bank let the team ship in roughly four weeks after a pivot and keeps them outside Money Services Business (MSB) status, since they never control user funds.

hackernews · harshithl1777 · Nov 24, 20:44

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 that standardizes how LLMs connect to external tools, data sources and workflows, often described as a "USB-C port" for AI apps. Passkeys are FIDO/WebAuthn credentials that replace passwords with cryptographic signatures verified by a device's biometrics, so approving a payment signs with a key stored on the user's phone. Versine's wallet holds USDC, a dollar-pegged stablecoin, on Base, an Ethereum Layer 2 network chosen for low transaction fees.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAuthn">WebAuthn - Wikipedia</a></li>
<li><a href="https://www.circle.com/blog/how-ai-agents-hold-and-spend-money">How Do AI Agents Pay: Wallets, Budgets, and Permissions | Circle</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly intrigued but pressed on the hard parts: a former payments fraud engineer asked what the reversal flow looks like when an agent pays the wrong person, and others warned that on/off-ramping will require full KYC that limits scaling and likely excludes non-US users. A security-minded commenter also questioned whether the passkey actually signs the amount and recipient shown on screen or only a session challenge, since an agent could otherwise swap the payment between display and approval.

**Tags**: `#MCP`, `#fintech`, `#AI agents`, `#payments`, `#startups`

---

<a id="item-9"></a>
## [songe: a training engine that improves your local LLM using idle compute](https://github.com/sous-labs/songe) ⭐️ 6.0/10

A GitHub project called songe (from sous-labs) offers a training engine that runs on a user's own machine and uses idle compute to keep improving a local LLM, rather than requiring a cloud training cluster. The project was discussed on Hacker News, where it reached about 180 points and 57 comments introducing the idea of "dream epochs" of self-training. If it works, it would let individual developers and small teams continually adapt a local model to their own data and workflows without paying for GPU hours in the cloud, turning everyday idle hardware into a slow but continuous fine-tuning loop. It also touches a broader trend of bringing training, not just inference, onto consumer and edge devices. The project targets a user's own model rather than training a foundation model from scratch, so gains would come from incremental self-training on locally generated or curated examples. Notably, the repository does not yet publish benchmarks or before/after examples, so the size of the improvement per "dream epoch" and the minimum viable hardware (GPU versus CPU-only) remain unquantified.

hackernews · bluepeter · Nov 24, 15:03 · [Discussion](https://news.ycombinator.com/item?id=50629231)

**Background**: A local LLM is a model such as a Qwen or Llama variant that runs on your own machine through tools like Ollama or llama.cpp, typically quantized to roughly 0.5GB of VRAM per billion parameters at 4-bit precision. Full pretraining of an LLM requires large multi-GPU clusters, but fine-tuning a small pre-trained model on modest data is far cheaper, and the search results note that techniques like QLoRA have made this practical on a single GPU. songe sits in that fine-tuning space: instead of a one-off training run, it tries to harvest idle cycles on the user's machine for continuous, incremental improvement.

<details><summary>References</summary>
<ul>
<li><a href="https://apxml.com/courses/llm-model-sizes-hardware/chapter-4-llm-inference-vs-training/hardware-training">Hardware Requirements for LLM Training - apxml.com</a></li>
<li><a href="https://airbyte.com/data-engineering-resources/how-to-train-llm-with-your-own-data">How to Train an LLM on Your Own Data (2026 Guide) | Airbyte</a></li>
<li><a href="https://nerdleveltech.com/running-llms-locally-the-complete-2025-guide">Running LLMs Locally: The Complete Practitioner's Guide</a></li>

</ul>
</details>

**Discussion**: Commenters were interested but wanted proof: one asked whether this could become a SETI@home-style distributed effort, others pressed for rough numbers on improvement per "dream epoch" or over a weekend of training, and one asked for a transcribed before/after example in the README so the improvement-judging process is shown rather than described. A practical concern was raised about whether it is worth running on modest hardware, such as a small Qwen model via Ollama on an ordinary Windows PC or a GPU-less VPS, with most of these questions left unanswered in the thread.

**Tags**: `#local-llm`, `#training-engine`, `#distributed-computing`, `#open-source`, `#hackernews`

---

<a id="item-10"></a>
## [Trump's Nvidia Intervention Ties His Political Fate to the AI Boom](https://www.bbc.co.uk/news/articles/ckj05m2zdyryo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

According to the BBC, President Trump personally intervened to reinstate Nvidia CEO Jensen Huang, an act the article describes as inextricably linking the president's political fortunes with the CEO's and with the wider AI boom. The report frames the episode as a case study in how directly the White House now involves itself in the fortunes of America's most valuable chip company. Nvidia sits at the center of the global AI buildout and of US equity markets, so any presidential action touching the company carries consequences for investors, chip supply chains and the broader tech industry. By staking his own credibility on Nvidia's chief executive, Trump has made AI policy — including export rules and chip deals — an explicitly political battleground ahead of future elections. The BBC piece is a short analytical news story and does not detail the precise mechanism or legal basis of the intervention, nor does it offer technical specifics about Nvidia's products or the affected export rules. Readers should treat the framing as political commentary rather than a definitive account of what changed in policy.

rss · BBC Business · Nov 25, 01:03

**Background**: Nvidia designs the graphics processors and AI accelerators that power most large-scale AI models, and its valuation has soared past $4 trillion, making it one of the largest companies in the world and a major driver of US stock indices. Because Washington restricts exports of advanced AI chips to China, Nvidia's access to that market depends heavily on decisions made by the White House rather than on the company alone. Trump has repeatedly inserted himself personally into tech-sector deals and export negotiations, so his administration is now a direct variable in how the AI industry grows.

**Tags**: `#AI industry`, `#Nvidia`, `#US politics`, `#tech policy`, `#geopolitics`

---

<a id="item-11"></a>
## [Heart Attack and Stroke Risk Can Be Predicted Decades in Advance](https://www.ed.ac.uk/news/heart-attack-and-stroke-risk-detectable-decades-in-advance) ⭐️ 5.0/10

A University of Edinburgh study reports that routine risk factors measured in healthy people can predict heart attack and stroke risk decades before an event occurs. The researchers found that a combination of common clinical measures — including blood pressure, cholesterol, inflammation markers and other routine readings — carries predictive signal over very long time horizons. If long-range risk can be estimated from cheap, routine tests, preventive treatment and lifestyle changes could start decades earlier, shifting cardiovascular care from reacting to events toward long-term prevention. Because cardiovascular disease remains a leading cause of death worldwide, even modest improvements in early targeting could affect very large populations. The risk factors examined include blood pressure, total and HDL cholesterol, inflammation measured by CRP, BMI, troponin and diabetes or smoking status, several of which can be combined into long-horizon risk scores such as the PREVENT equations. The practical value of such predictions depends on whether they change what doctors and patients actually do, since the underlying risk factors are well known and only partially modifiable.

hackernews · gmays · Nov 24, 21:51 · [Discussion](https://news.ycombinator.com/item?id=50635271)

**Background**: Cardiovascular risk scores are standard tools in primary care: they combine factors such as age, blood pressure, cholesterol and smoking into an estimate of the chance of a heart attack or stroke within a fixed period, usually 10 years. The PREVENT equations, developed by the American Heart Association, extend this to 30-year estimates and can include additional markers such as kidney function and inflammation. Statins are the most common preventive drug, lowering LDL cholesterol, while newer options such as GLP-1 receptor agonists target weight and metabolic health.

**Discussion**: Commenters were split: some saw clear practical value, pointing out that most of the listed risk factors are highly modifiable and that tools like the PREVENT equations already turn these numbers into a 30-year risk estimate, while others argued the study merely restates what everyone already knows about blood pressure, cholesterol and lifestyle. Personal anecdotes featured prominently, including one commenter's difficult experience with statin side effects and a subsequent switch toward a mostly plant-based diet, and several pushed GLP-1 drugs as an underused first-line answer to metabolic disease.

**Tags**: `#cardiovascular health`, `#risk prediction`, `#medical research`, `#statins`, `#preventive medicine`

---

<a id="item-12"></a>
## [Jetty Pro, a New Mac Dock Alternative, Sparks Subscription Pricing Debate](http://hypercritical.co/2026/11/23/jetty-pro) ⭐️ 5.0/10

Jetty Pro is a newly announced Mac utility that serves as an alternative to the macOS Dock UI, and its Hacker News submission reached 274 points with around 120 comments. The thread quickly shifted from the app itself to debates over subscription licensing and interest in lightweight, custom-built native Mac tools. The reaction illustrates how sensitive Mac users have become to subscription pricing for small utility apps, where even a one-dollar-a-year fee can be a dealbreaker. It also shows a growing willingness among developers to replace bloated commercial apps with small native tools generated with help from AI coding assistants. Commenters noted that the product page never states up front that Jetty Pro is a Dock replacement, and that the app lacks a demo video showing off its features. One suggested compromise was a fallback perpetual license, letting users keep the build they had when their subscription lapsed.

hackernews · zdw · Nov 24, 16:23 · [Discussion](https://news.ycombinator.com/item?id=50630462)

**Background**: The macOS Dock is the strip of application icons typically anchored at the bottom of the screen, used to launch and switch between apps; alternatives to it have long been a niche category of Mac utilities. Subscription licensing has become common for indie Mac apps because it provides recurring revenue for ongoing compatibility work as macOS changes. Jetty Pro's discussion also touches on "vibe coding" — using large language models such as Claude or OpenAI Codex to generate small purpose-built native apps.

**Discussion**: Sentiment was largely positive toward the developer's effort but firmly against the subscription model, with one commenter saying they "simply cannot justify yet another subscription," regardless of price. Others asked for a demo video, complained the page should lead by explaining it replaces the Dock, and one described recently replacing several apps with Claude-built native Mac apps that are faster and use far less memory.

**Tags**: `#Mac apps`, `#subscription software`, `#native development`, `#product launch`, `#Hacker News`

---

<a id="item-13"></a>
## [Tech sell-off resumes as Nvidia rally fades after Huang's return](https://www.theguardian.com/business/2026/nov/24/nvidia-stock-falls-jensen-huang) ⭐️ 5.0/10

Nvidia stock fell almost 6% on Tuesday, and technology shares led a broader market retreat, one day after Jensen Huang's reinstatement as CEO had driven Nvidia up more than 30% and added over $900bn in market value. The sharp reversal shows how sensitive AI-linked stocks are to leadership news and investor sentiment, and continued volatility in the AI sector could affect the wider market because it is a major driver of global economic growth. The report frames the move as a sentiment-driven swing rather than a fundamental change, with investors bracing for further volatility after the brief euphoria over Huang's return.

rss · The Guardian Business · Nov 24, 22:05

**Background**: A sell-off is a rapid wave of selling in securities such as stocks, often accompanied by high trading volume, that pushes prices down quickly. Market capitalization is the total value of a publicly traded company's outstanding shares, so a 30% share-price rise can add hundreds of billions of dollars in paper value for a giant company like Nvidia. Nvidia is closely watched as a bellwether for AI-related investment, which helps explain why its swings can move the broader technology sector.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/s/sell-off.asp">Sell-Off: Definition, How It Works, Triggers, and Example</a></li>
<li><a href="https://en.wikipedia.org/wiki/Market_capitalization">Market capitalization - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI industry`, `#stock market`, `#tech sell-off`, `#Jensen Huang`

---

<a id="item-14"></a>
## [EU to Cap Chinese Hybrid Vehicle Imports With Temporary Quotas](https://www.theguardian.com/business/2026/nov/24/eu-cap-chinese-hybrid-ev-imports-tariff-uk) ⭐️ 5.0/10

The European Commission announced that next month the EU will impose temporary quotas on Chinese hybrid car imports, with the same caps also applying to hybrids from Japan, Turkey, South Korea and the UK. The measure is a trade-policy intervention aimed at curbing a post-October rise in Chinese hybrid exports, affecting automakers, importers and consumers across the EU as well as suppliers in the UK, Japan, Turkey and South Korea. The report does not specify quota volumes or duration; EU safeguard quotas are temporary quantitative restrictions meant to give domestic industry breathing space, and the fact that the caps cover several non-EU origins is consistent with safeguard-style measures that apply to all imports of the product concerned.

rss · The Guardian Business · Nov 24, 10:59

**Background**: Safeguards are one of the EU’s trade-defence instruments and can take the form of import or tariff quotas designed to address a sudden, sharp increase in imports. The EU has already used countervailing duties against Chinese battery-electric vehicles, and this action extends trade defences to hybrid cars. Hybrids range from mild hybrids, which use a small electric motor mainly as assistance, to full hybrids and plug-in hybrids that can drive on electric power, so the quota’s scope will determine which models are affected.

<details><summary>References</summary>
<ul>
<li><a href="https://policy.trade.ec.europa.eu/enforcement-and-protection/trade-defence/safeguards_en">Safeguards - Trade and Economic Security - European Commission</a></li>
<li><a href="https://policy.trade.ec.europa.eu/enforcement-and-protection/trade-defence/safeguards/safeguard-measures_en">Safeguard measures - Trade and Economic Security - European ...</a></li>
<li><a href="https://jalopnik.com/2058138/full-mild-hybrid-vs-plug-in-difference/">Full Vs. Mild Vs. Plug-In Hybrids: What's The Difference?</a></li>

</ul>
</details>

**Tags**: `#EU trade policy`, `#Chinese EVs`, `#hybrid vehicles`, `#tariffs and quotas`, `#automotive industry`

---

<a id="item-15"></a>
## [Victoria election could decide fate of nine datacentre projects](https://www.theguardian.com/australia-news/2026/nov/24/nine-datacentre-projects-awaiting-approval-victoria-election) ⭐️ 5.0/10

Nine datacentre projects are awaiting planning approval in Victoria as the state heads to the polls on Saturday, and some developers remain confident they will be greenlit despite growing community backlash. Opinion polls predict the Coalition will take power from the 12-year-old Labor government, leaving open whether the Liberal and National parties' datacentre policy would apply to applications already in the queue. State-level planning decisions like these directly control how fast AI-driven datacentre capacity gets built in one of Australia's main markets, so the election result shapes the project pipeline for operators, utilities and investors. It also tests whether political support for the sector, as signalled by the Coalition, can override community resistance over energy and water use. A central uncertainty is whether a newly elected Coalition government's datacentre policy would be applied retroactively to the nine existing applications rather than only to future ones. The most recent datacentre approval in Victoria was granted on 6 May to PGIM Real Estate, part of US financial giant Prudential Financial, for a project in Melbourne's west.

rss · The Guardian World · Nov 25, 00:42

**Background**: Datacentre planning approvals in Australia are handled at the state level, which means elections can quickly reshape which projects proceed and which stall. Victoria has built a visible backlog of stalled proposals, and opposition to datacentres over their electricity and water demands has moved from marginal to mainstream during 2026, with several communities successfully pushing back. In March 2026 the federal government published guidelines for datacentre developers that flagged community trust alongside clean energy, water use, local skills and security as key expectations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/australia-news/2026/nov/20/communities-are-really-angry-how-datacentre-opposition-has-gone-from-marginal-to-mainstream-in-five-months">‘Communities are really angry’: how Australia’s datacentre ...</a></li>
<li><a href="https://ia.acs.org.au/article/2026/data-centres-need-community-approval--not-just-legal-permission.html">Data centres need community approval, not just legal ...</a></li>
<li><a href="https://www.afr.com/companies/infrastructure/the-one-thing-propping-up-victoria-s-economy-is-on-ice-20261103-p61a1m">Victorian data centre backlog grows as stalled project ...</a></li>

</ul>
</details>

**Tags**: `#datacentres`, `#infrastructure-policy`, `#australia`, `#energy`, `#regulation`

---