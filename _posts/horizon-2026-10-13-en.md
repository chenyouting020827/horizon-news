# Horizon Daily - 2026-10-13

> From 154 items, 17 important content pieces were selected

---

1. [A Modern Web App in C: CGI, FastCGI and Privilege Dropping](#item-1) ⭐️ 8.0/10
2. [OpenAI's Codex CLI silently installs a persistent, self-updating background daemon](#item-2) ⭐️ 8.0/10
3. [Z.ai Releases GLM-Legal, Sparking Debate on Trust and Legal AI](#item-3) ⭐️ 7.0/10
4. [Hackers Trigger Defrost Cycles in European Supermarket Fridges](#item-4) ⭐️ 7.0/10
5. [WiFi 7 Router Hacked into a 320 Msps SDR Receiver](#item-5) ⭐️ 7.0/10
6. [Blog argues using AI well is a skill, sparking Hacker News debate](#item-6) ⭐️ 7.0/10
7. [Microsoft to shift AI inference to its homegrown Maia chips](#item-7) ⭐️ 7.0/10
8. [Decoding AVX-512's cryptic 'vfmaddrnd231pd' instruction name](#item-8) ⭐️ 6.0/10
9. [Blog Walks Through Building a Demoscene Intro for the ZX Spectrum](#item-9) ⭐️ 6.0/10
10. [IonQ to acquire Elisity in all-stock deal worth up to $1.3B](#item-10) ⭐️ 6.0/10
11. [Microsoft president: AI is less regulated than milk, urges global rules](#item-11) ⭐️ 6.0/10
12. [Making Big Downloads Resumable in Firefox: A TIL Tutorial](#item-12) ⭐️ 5.0/10
13. [Agent37 (YC F26) launches low-cost sandboxes for AI agents](#item-13) ⭐️ 5.0/10
14. [Citroën revives the iconic 2CV as a sub-tonne electric car](#item-14) ⭐️ 5.0/10
15. [Meta debuts Muse Wonder AI model behind a paid Muse subscription](#item-15) ⭐️ 5.0/10
16. [Intel, Broadcom CEOs Warn Capital Crunch Could Bottleneck AI Boom](#item-16) ⭐️ 5.0/10
17. [UK AI minister warns cyber defences 'likely' to be breached](#item-17) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [A Modern Web App in C: CGI, FastCGI and Privilege Dropping](https://prophitt.me/writing/a-modern-web-app-in-c) ⭐️ 8.0/10

An article on prophitt.me walks through building a modern web application in plain C, and it drew a large Hacker News discussion (roughly 358 points and 156 comments) about CGI, FastCGI, privilege separation and deployment tradeoffs. Practitioners used the thread to compare the C approach with alternatives such as BusyBox's built-in CGI support and single-binary Go servers. The piece is a reminder that a full web service does not require a heavyweight framework or runtime stack, which matters for developers who value small attack surfaces, minimal dependencies and long-lived, easily auditable code. It also revives a design debate between CGI/FastCGI-style process models and modern single-binary or containerized deployments. The article emphasizes dropping privileges (for example via pledge, chroot and similar mechanisms) so that the web-facing process runs with the least authority necessary, and commenters noted that FastCGI avoids the cost of spawning a new process per request that plain CGI incurs. A recurring caveat is that C makes concurrent programming harder, since forked processes must reinitialize writable .bss and .data segments even though read-only .text can be shared.

hackernews · prophittcorey · Oct 12, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50058528)

**Background**: CGI (Common Gateway Interface) is a long-standing standard that lets a web server run an external program to handle a request and return its output as the HTTP response. FastCGI is a language-independent extension of CGI that keeps processes alive between requests instead of starting a new one each time, improving performance. Privilege separation is a security practice in which a program forks into two processes: one keeps elevated privileges for a narrow task while the main, exposed process drops them, limiting the damage if it is compromised.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inmotionhosting.com/support/website/what-is-cgi.md">inmotionhosting.com/support/website/ what - is - cgi .md</a></li>
<li><a href="https://www.hostingadvice.com/how-to/what-is-fastcgi/">What Is FastCGI ? How FastCGI Transforms Server Efficiency</a></li>
<li><a href="https://en.wikipedia.org/wiki/Privilege_separation">Privilege separation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agreed the article's reasoning was sound, especially its treatment of privilege dropping, and several shared war stories: one developer described running a C/FastCGI ordering system for 22 years, while others pointed out that BusyBox ships built-in CGI support and that Go can serve a site from a single binary without libc. The main counterargument to the C approach was the difficulty of concurrency in C and the appeal of stacking managed layers or using Go instead.

**Tags**: `#C`, `#web development`, `#CGI`, `#FastCGI`, `#systems programming`

---

<a id="item-2"></a>
## [OpenAI's Codex CLI silently installs a persistent, self-updating background daemon](https://github.com/openai/codex/issues/48195) ⭐️ 8.0/10

A GitHub issue (openai/codex #48195) reports that Codex CLI now starts a persistent background daemon by default via `codex app-server --managed-daemon`, which runs in its own session with no TTY and keeps running even after every Codex window is closed, until it is stopped explicitly or the machine reboots. The issue, filed around September 25, 2026, asks OpenAI to make the `daemon_auto_start` behavior opt-in rather than default. Because Codex CLI is a widely used AI coding agent that runs locally in the terminal, a silently enabled always-on daemon changes the trust model for every developer who installs it: background processes, disk usage and auto-updates now happen without explicit consent. The issue's 426 points and 222 comments show that default-on background services in developer tooling are becoming a flashpoint for privacy, resource and reliability concerns across the AI coding tool ecosystem. There is no documented setting to disable the daemon, but it currently sits behind a feature flag that can be flipped in `~/.codex/config.toml` with `[features]` / `daemon_auto_start = false`. Users also report that the daemon writes pid and lock files under `~/.codex` at startup and have suggested deleting them and replacing them with symlinks to `/dev/null` marked immutable via `chattr +i` as a workaround.

hackernews · whimblepop · Oct 12, 18:29 · [Discussion](https://news.ycombinator.com/item?id=50060694)

**Background**: Codex CLI is OpenAI's open-source AI coding agent that runs in the terminal, able to read and modify files and execute commands locally; it is part of the broader Codex software-development platform alongside IDE extensions, a desktop app and cloud-based development. A daemon is a long-running background process that is not attached to an interactive terminal, commonly used to keep a service warm or perform periodic tasks such as syncing or self-updating. Self-updating daemons are a known operational pain point: they can fail to apply updates, restart the wrong service instance, or, as here, consume disk space by retaining old versions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex/issues/48195">CLI: make `daemon_auto_start` opt-in — a persistent, self ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_CLI">Codex CLI</a></li>
<li><a href="https://docs.atuin.sh/main/reference/daemon/">daemon - Atuin Docs</a></li>

</ul>
</details>

**Discussion**: Commenters are broadly critical: one reports the daemon consuming roughly 12 GB of disk on their machine with old versions, another says auto-updating randomly corrupts permissions and makes `.git` read-only, blocking work for hours at a time. Others share concrete mitigations (the `daemon_auto_start = false` flag, symlinking state files to `/dev/null` with `chattr +i`) and a counterpoint that minimal, bash-driven harnesses like hax are a breath of fresh air compared with such overengineered tooling.

**Tags**: `#codex-cli`, `#openai`, `#background-daemon`, `#developer-tools`, `#privacy`

---

<a id="item-3"></a>
## [Z.ai Releases GLM-Legal, Sparking Debate on Trust and Legal AI](https://z.ai/blog/glm-legal) ⭐️ 7.0/10

Z.ai (the international brand of Beijing-based Zhipu AI) announced GLM-Legal, a large language model fine-tuned for the legal domain, in a post on its official blog. The release drew heavy Hacker News attention, with the thread reaching 403 points and 228 comments. It marks another step in the trend of vertical, domain-specific LLMs moving into high-stakes professional fields such as law, where errors have direct financial and legal consequences. It also puts a spotlight on vendor trust: a legal product handles privileged and sensitive material, so the reputation of the company behind the model becomes as important as its benchmark scores. Discussion threads reference benchmark results that one commenter, an attorney, describes as roughly a 20% pass rate, which he considers unimpressive for litigation practice. Commenters also note that Anthropic's updated usage policy requires a qualified 'human in the loop' when AI outputs can affect someone's legal rights, health, or finances — a constraint that frames how tools like GLM-Legal can realistically be deployed.

hackernews · ilreb · Oct 12, 16:11 · [Discussion](https://news.ycombinator.com/item?id=50058507)

**Background**: GLM stands for General Language Model, a family of pretrained dialogue models first developed by Zhipu AI together with Tsinghua University's KEG lab in 2023 and formerly known as ChatGLM; Z.ai is Zhipu's consumer-facing brand, and the line has since produced releases such as GLM-4.5 and GLM-4.6. 'Domain-specific' or 'vertical' LLMs like GLM-Legal take a general-purpose base model and further train it on specialized corpora such as statutes, contracts, and case law. The Hacker News debate also references a widely circulated report that Z.ai's coding tool snapshotted users' entire workspaces before every prompt, which critics cite as evidence of poor privacy practices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z.ai - Wikipedia</a></li>
<li><a href="https://theairankings.com/zhipu/">Zhipu AI (Z. ai ) in 2026: GLM Models, IPO, Funding... | The AI Rankings</a></li>
<li><a href="https://www.layer3labs.io/guides/z-ai-explained">Z. AI Explained: Zhipu , GLM Models, Safety & Pricing</a></li>

</ul>
</details>

**Discussion**: Sentiment is mixed and skeptical: several commenters want benchmarks split into generic versus novel tasks, and an attorney dismisses a reported 20% pass rate as far from litigation-grade. Others question whether a legal product can be trusted from a vendor accused of silently snapshotting entire workspaces before every prompt. On the positive side, some argue LLMs could genuinely help clear massive court backlogs — one commenter cites India's roughly 58 million pending cases — while acknowledging the need for human review per Anthropic's policy.

**Tags**: `#LLM`, `#legal-tech`, `#AI applications`, `#privacy`, `#domain-specific models`

---

<a id="item-4"></a>
## [Hackers Trigger Defrost Cycles in European Supermarket Fridges](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 7.0/10

Attackers reportedly gained access to internet-connected Danfoss refrigeration controllers and remotely activated automatic defrost cycles at supermarket chains across Europe, notably in France, where reports say around 150 Intermarché stores were targeted and nearly 400 stores overall were affected. The incident disrupted cold storage, in-store pricing and delivery operations, and was linked to legacy controllers with known vulnerabilities. This is a rare real-world case where an operational technology (OT) attack on mundane retail equipment caused direct physical and commercial damage, showing that internet-connected building and refrigeration systems are now viable targets. It highlights a systemic problem: critical infrastructure protection advice has long focused on power grids and factories, while grocery cold chains, hospitals and other essential services run on the same unpatched, vendor-managed hardware. Discussion points to suspects such as the Danfoss SM800 (end of support 2021) and SC355 (end of support 2016) controllers, whose flaws were documented in security research on refrigeration controllers; reports describe freezer temperatures being pushed as high as roughly 50°C, forcing stock to be discarded. Because the controllers were intentionally connected to the internet for remote diagnostics and efficiency monitoring — as Danfoss itself markets — the attack surface was created by the vendor's own value proposition, not only by customer negligence.

hackernews · Zeekaas · Oct 12, 12:16 · [Discussion](https://news.ycombinator.com/item?id=50055304)

**Background**: Operational technology (OT) refers to the hardware and software that monitor and control physical processes, such as the refrigeration controllers managing supermarket freezers, compressors and temperature alarms. Unlike IT systems, OT equipment is often expected to run for 15–20 years, is rarely patched, and is increasingly connected to the internet so vendors and service engineers can diagnose faults without a site visit. Control system security is the discipline of protecting these devices, and it traditionally lags far behind conventional IT security in patching cadence and visibility.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/security/danfoss-refrigeration-hack-france-supermarkets/">Refrigeration Cyberattack Hits French Supermarkets | Cybernews</a></li>
<li><a href="https://www.it-connect.tech/super-u-and-intermarche-hit-by-cyberattack-that-turned-freezers-into-ovens/">Cyberattack Disrupts Danfoss Refrigeration at Super U ...</a></li>
<li><a href="https://cybersecuritynews.com/supermarket-fridges-hacked/">Attackers Reportedly Hack Supermarket Fridges and Raise ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely rejected the flippant "why would you connect a freezer to the internet?" framing, arguing that the root cause is security debt and maintenance economics: 15–20 year old controllers with known CVEs are kept running because there is no margin to replace them, while vendors push connectivity for remote diagnostics. A hospital lab technician's anecdote about subscription-locked lab machines needing internet access illustrated that this pattern extends well beyond refrigeration, and others speculated whether the attack is linked to a similar August 2026 incident at US military base freezers.

**Tags**: `#cybersecurity`, `#IoT/OT security`, `#critical infrastructure`, `#vulnerability management`, `#supply chain`

---

<a id="item-5"></a>
## [WiFi 7 Router Hacked into a 320 Msps SDR Receiver](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 7.0/10

Developer h0m3us3r has published a project that repurposes the W1700K WiFi 7 router into a software defined radio receiver capable of sampling at 320 Msps around the 5 GHz band. The same developer previously built eSpDR, an SDR implementation running on an ESP32 Wi-Fi microcontroller, suggesting a pattern of turning commodity wireless chipsets into low-cost radio front ends. It shows that hardware people already own — consumer routers and laptops with Wi-Fi cards — can be repurposed into surprisingly capable SDR receivers, dramatically lowering the cost of entry for RF experimentation and spectrum monitoring. If the approach spreads to common Wi-Fi chipsets, hobbyists, students and researchers could gain a ubiquitous, cheap alternative to dedicated SDR hardware such as USRP or high-end RTL-SDR setups. The receiver runs at 320 Msps in the 5 GHz band, a combination that is unusually cheap to achieve for that sample rate and frequency. The community notes the W1700K uses the same chipset as the Banana Pi R4, which has built-in PCIe for NVMe storage, so the technique is likely portable to that board; a 320 Msps rate is still well below the Nyquist rate needed to directly digitize all of 5 GHz, so practical use implies downconversion or sub-Nyquist techniques.

hackernews · djfergus · Oct 12, 12:41 · [Discussion](https://news.ycombinator.com/item?id=50055593)

**Background**: Software defined radio (SDR) replaces analog mixers, filters and modulators with software running on a general-purpose computer or embedded system, so the same hardware can receive and decode many different radio standards. Sample rate (measured in megasamples per second, Msps) determines how much instantaneous bandwidth a receiver can capture, while the tuning band determines which signals it can reach. The W1700K is a WiFi 7 router that has drawn attention in the OpenWrt community as a potential 10G-capable device, though support is still described as rough.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio - Wikipedia</a></li>
<li><a href="https://www.accio.com/business/openwrt-tenda">OpenWrt Tenda Router Guide 2026</a></li>

</ul>
</details>

**Discussion**: Commenters were enthusiastic: one pointed out the same developer's ESP32-based eSpDR project and wished more common Wi-Fi cards could be used as SDRs so any laptop could become a budget radio. Others noted the shared chipset likely makes it work on the Banana Pi R4, and an experienced service-monitor repairer sketched how to extend the setup into a full service monitor with attenuators, a 5 GHz low-pass filter, and a 7–12 GHz local oscillator/mixer up/down converter; one commenter also mused that phone makers restrict FM radio access partly because modern phone radios are software defined.

**Tags**: `#SDR`, `#WiFi 7`, `#hardware hacking`, `#RF`, `#embedded systems`

---

<a id="item-6"></a>
## [Blog argues using AI well is a skill, sparking Hacker News debate](https://yyhh.org/blog/2026/10/ai-is-a-tool/) ⭐️ 7.0/10

A blog post published at yyhh.org titled "AI is a tool and using it well takes skill" argues that AI is a tool whose effective use requires real, developed skill rather than passive reliance. The post triggered a Hacker News discussion that reached 181 points with roughly 170 comments, making it a highly active thread. The debate goes to the heart of how quickly AI-driven workflows are reshaping knowledge work, especially software engineering, and asks whether the skills workers are currently investing in will still be worth anything in six months. It also raises the stakes for education and cognition, with commenters worried that rapid adoption could produce a long-term decline in human reasoning and study habits. Several commenters claim that earlier prompt-engineering craft — context management, special instruction "recipes", agent graphs and vector search pipelines — has already become obsolete, and that the current meta is simply "knowing what to ask for". Others counter that the comparison is misleading, likening AI-assisted development to professional photography: everyone owns a camera, but years of domain experience still separate professionals from casual users.

hackernews · layer8 · Oct 12, 21:40 · [Discussion](https://news.ycombinator.com/item?id=50063427)

**Background**: Hacker News is a technology news aggregator run by Y Combinator where submissions are ranked by points and dissected in long threaded comment sections, so a score of 181 points with ~170 comments signals a genuinely contested topic. Large language models (LLMs) such as ChatGPT and Claude are driven by natural-language prompts, and "prompt engineering" was the term for the craft of wording those prompts, managing context windows and building tool or retrieval pipelines. As model quality has improved, much of that scaffolding has been absorbed by the models themselves, which is exactly what the commenters are arguing about. The thread also touches on education research concerns previously raised about smartphones and social media and their effect on attention.

**Discussion**: Sentiment is split but leans skeptical of the idea that AI use is a durable skill: extr and whatever1 report that techniques they had carefully learned were rendered obsolete within months, with whatever1 noting a single six-word prompt now root-causes a log in about ten minutes. jgord warns that AI may spread faster than users can learn to use it in ways that increase rather than decrease human knowledge, predicting a decades-long dip in cognitive ability and a worse educational impact than smartphones. mosesman counters with the professional-photography analogy — experience still matters — while im_down_w_otp compares interacting with models to pulling the lever on a slot machine.

**Tags**: `#AI`, `#LLM`, `#productivity`, `#education`, `#human-computer interaction`

---

<a id="item-7"></a>
## [Microsoft to shift AI inference to its homegrown Maia chips](https://www.cnbc.com/2026/10/12/microsoft-will-mainly-use-its-maia-chips-for-ai-inference.html) ⭐️ 7.0/10

Microsoft announced on October 12, 2026 that it will scale its Azure Maia chip family to multi-gigawatt deployments starting in 2027, making Maia the primary inference system for Microsoft products and services. Maia 200 is now in production, and the next-generation Maia 300 is slated for 2027. A major hyperscaler moving its AI inference workloads onto in-house silicon signals margin expansion and a meaningful reduction in reliance on Nvidia's near-monopoly in AI accelerators. It also strengthens Microsoft's vertically integrated AI stack and pressures other cloud providers and chip vendors to respond. Maia is positioned primarily for inference rather than training workloads, which are less demanding on interconnect and memory bandwidth than frontier model training. Microsoft's first Maia 100 chip debuted in April 2024, built on TSMC's 5nm node with advanced packaging, and was designed using lessons from running large-scale workloads such as Microsoft Copilot.

rss · CNBC Top News · Oct 12, 14:04

**Background**: AI workloads split into training, where a model learns from massive datasets, and inference, where a trained model answers real-world requests at scale; inference is the ongoing, high-volume cost center for services like Copilot. Hyperscalers have been designing custom accelerators — Google's TPUs, AWS's Trainium and Inferentia, and Microsoft's Maia — to cut costs and gain leverage against Nvidia, whose GPUs have dominated AI infrastructure. Building in-house silicon is a multi-year, capital-intensive effort because it requires chip design, software toolchains, and data-center integration to mature together.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/">Microsoft to expand Azure Maia system to multi-gigawatt ...</a></li>
<li><a href="https://azure.microsoft.com/en-us/blog/azure-maia-for-the-era-of-ai-from-silicon-to-software-to-systems/">Azure Maia for the era of AI: From silicon to software to systems</a></li>
<li><a href="https://www.msn.com/en-us/news/other/microsoft-unveils-new-maia-ai-chips-what-to-know/ar-AA2e4pjd">Microsoft unveils new Maia AI chips. What to know.</a></li>

</ul>
</details>

**Tags**: `#AI Hardware`, `#Semiconductors`, `#Microsoft`, `#Nvidia`, `#AI Infrastructure`

---

<a id="item-8"></a>
## [Decoding AVX-512's cryptic 'vfmaddrnd231pd' instruction name](https://purplesyringa.moe/blog/who-is-vfmaddrnd231pd/) ⭐️ 6.0/10

A blog post by purplesyringa dissects the AVX-512 mnemonic 'vfmaddrnd231pd', explaining what every encoded component of the name actually means. It breaks the string into its parts — the vector fused multiply-add operation, embedded rounding, the operand-ordering digits, and the data type — showing why the name is so long and unreadable at a glance. Instruction names like this sit at the boundary between human-readable assembly and encoded machine state, so understanding them helps low-level, compiler and performance developers read disassembly, debug generated code, and reason about what the CPU actually computes. It is a niche topic, but a good illustration of how hardware features such as embedded rounding get baked directly into mnemonic naming rather than handled by separate control settings. 'vfmadd' stands for vector fused multiply-add, 'rnd' signals embedded (static) rounding, the trailing 'pd' means packed double-precision floats, and the three digits '231' encode the ordering of the source and destination register operands in the multiply-add. The suffix is necessary because AVX-512's EVEX encoding lets the rounding mode be specified inside the instruction itself, so a distinct mnemonic per rounding variant must exist instead of relying on a global control register.

hackernews · pngmangi · Oct 12, 21:12 · [Discussion](https://news.ycombinator.com/item?id=50063138)

**Background**: AVX-512 is Intel's 512-bit SIMD extension to the x86 instruction set, extending earlier SSE and AVX vector instructions and using a new 4-byte EVEX prefix that allows access to 32 wide ZMM registers, opmask registers, operand broadcasting, and embedded rounding and exception control. A fused multiply-add (FMA) instruction computes a multiply and an add in a single step with only one rounding, which improves both accuracy and throughput. Because AVX-512 lets the rounding mode be encoded in the instruction, Intel had to invent extra-long mnemonic names to distinguish variants — the source of the naming pattern this article unpacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AVX-512">AVX-512 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/EVEX_prefix">EVEX prefix - Wikipedia</a></li>
<li><a href="https://www.intel.com/content/www/us/en/developer/articles/technical/intel-avx-512-instructions.html">Intel® AVX-512 Instructions</a></li>

</ul>
</details>

**Discussion**: Discussion was minimal (only three comments) and largely tangential. The one substantive comment, from Lerc, laments that incomprehensible names like this force a mental translation step and reflects a broader worry that people increasingly never interact with low-level abstractions directly — a theme he notes is usually discussed in the context of AI today.

**Tags**: `#x86`, `#assembly`, `#AVX-512`, `#CPU architecture`, `#instruction encoding`

---

<a id="item-9"></a>
## [Blog Walks Through Building a Demoscene Intro for the ZX Spectrum](https://www.markround.com/blog/2026/zx-spectrum-intro) ⭐️ 6.0/10

Mark Round published a blog post that walks step by step through the craft of writing a demoscene intro for the ZX Spectrum, the 8-bit Sinclair home computer. The write-up focuses on the low-level programming and optimization work required to squeeze an audiovisual presentation out of very constrained hardware. It is a concrete, hands-on example of a retro-computing subculture that still shapes how programmers think about performance and code size, even as modern hardware makes such constraints rare. For developers raised on abundant memory and CPU cycles, the demoscene's discipline of doing more with less remains an influential counterpoint to today's 'just add hardware' mindset. The ZX Spectrum is built around a Zilog Z80 CPU with only 16 KB to 128 KB of RAM depending on the model, no dedicated graphics or sound chips, and video output to a television, so demoscene effects must be produced largely in software. Traditional demoscene categories such as the 4K and 64K intro impose strict executable-size limits that make every byte count.

hackernews · zdw · Oct 12, 19:40 · [Discussion](https://news.ycombinator.com/item?id=50061859)

**Background**: The demoscene is an international computer art subculture that began with the early-1980s home computer boom and the software-cracking scene, whose 'cracktros' evolved into standalone audiovisual demos used to show off programming, graphics and music skills. Programs are shared and voted on at events called demoparties. The ZX Spectrum, launched by Sinclair Research in the UK in April 1982, was one of the best-selling British computers with over five million units sold, and Britain's top-selling computer until the 1990s.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demoscene">Demoscene - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ZX_Spectrum">ZX Spectrum</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread was small (roughly 64 points and 6 comments) and largely nostalgic and anecdotal: one commenter recalled being in high school when the demoscene took off in the 1980s and said it permanently colored his view of later developers as 'lazy' about optimization. Others shared links to specific productions on Demozoo and to Syntaxparty, a demoparty happening in Melbourne in a couple of weeks, while one commenter reflected on how the scene's influence spreads by word of mouth, with people in 2026 still enjoying demos made in 1992 and making new ones that look like they are from 1992.

**Tags**: `#demoscene`, `#zx-spectrum`, `#retro-computing`, `#assembly`, `#optimization`

---

<a id="item-10"></a>
## [IonQ to acquire Elisity in all-stock deal worth up to $1.3B](https://www.cnbc.com/2026/10/12/ionq-elisity-acquisition-cybersecurity.html) ⭐️ 6.0/10

IonQ, a quantum computing platform company, has agreed to acquire the cybersecurity firm Elisity in an all-stock deal valued at up to $1.3 billion, according to a CNBC report. The announcement marks one of the largest acquisitions to date by a pure-play quantum computing company. The deal signals that quantum computing vendors are moving beyond hardware research into adjacent enterprise security markets, giving IonQ a commercial cybersecurity revenue stream alongside its quantum systems business. It also highlights growing convergence between quantum technology and the identity-based network security segment, as enterprises brace for both current ransomware threats and future quantum-enabled attacks on cryptography. The consideration is entirely in IonQ stock rather than cash, and the stated value of "up to $1.3 billion" suggests part of the payout is contingent on milestones or performance targets rather than paid upfront. Neither company has disclosed integration details, such as how Elisity's microsegmentation platform would connect with IonQ's quantum cloud and hardware roadmap.

rss · CNBC Top News · Oct 12, 19:35

**Background**: IonQ is a publicly traded quantum computing company whose systems use trapped-ion technology: individual ions are held in place and manipulated with precisely controlled laser pulses to perform quantum gate operations. Elisity is a cybersecurity vendor specialising in identity-based microsegmentation, an approach that divides an enterprise network into small, policy-controlled zones so that attackers cannot move laterally or spread ransomware across IT, OT and IoT environments — a core building block of Zero Trust architectures. Quantum computing matters to security because a sufficiently powerful quantum computer could break widely used public-key cryptography such as RSA and ECC, which is why both quantum vendors and security firms are positioning themselves around the coming transition to post-quantum standards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ionq.com/">IonQ : Trapped Ion Quantum Computing Company</a></li>
<li><a href="https://www.elisity.com/">Simplify Network Segmentation | Elisity Identity-Based ...</a></li>
<li><a href="https://www.elisity.com/microsegmentation">Microsegmentation Guide: Zero Trust & Identity | Elisity</a></li>

</ul>
</details>

**Tags**: `#Quantum Computing`, `#Cybersecurity`, `#Mergers and Acquisitions`, `#IonQ`, `#Elisity`

---

<a id="item-11"></a>
## [Microsoft president: AI is less regulated than milk, urges global rules](https://www.bbc.co.uk/news/articles/c6rmy7zmvx3lo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

Microsoft president Brad Smith said AI is currently subject to less regulation than milk and called for global rules to govern the technology. He argued that the UK is in the "best position" to lead international efforts on AI regulation. A senior executive at one of the world's most influential AI companies publicly pushing for binding rules adds significant industry weight to the global AI governance debate. Because rules being drafted in the EU, the US and the UK will shape how AI models are built, deployed and sold worldwide, the stance of major vendors like Microsoft can influence how strict those rules ultimately become. The "less regulated than milk" framing is a rhetorical comparison: dairy products face detailed, enforceable food-safety standards, whereas AI systems are largely covered by voluntary commitments and patchy, sector-specific guidance. The report does not lay out specific legislative proposals, so the statement is best read as a directional push for coordinated international rules rather than a detailed policy blueprint.

rss · BBC Business · Oct 12, 07:47

**Background**: Brad Smith is Microsoft's president and vice chair and a frequent voice on technology policy; Microsoft is a major investor in and partner of OpenAI, making it one of the most powerful players in generative AI. Governments have moved at very different speeds on AI rules: the EU adopted a comprehensive AI Act, while the UK has favored a more sector-by-sector, pro-innovation approach and hosted the 2023 Bletchley Park AI Safety Summit, which led to the creation of the UK AI Safety Institute. The core question in this debate is whether AI needs binding global rules or whether flexible national frameworks are enough.

**Tags**: `#AI regulation`, `#policy`, `#Microsoft`, `#governance`, `#industry news`

---

<a id="item-12"></a>
## [Making Big Downloads Resumable in Firefox: A TIL Tutorial](https://lunarwatcher.codeberg.page/til/firefox/resumable-big-downloads.html) ⭐️ 5.0/10

A TIL-style article explains how to make large, interrupted downloads resumable in Firefox, addressing a long-standing browser limitation. The post has sparked discussion about Firefox's download resumption behavior and workarounds such as manually swapping .part files. This matters because users on flaky connections often lose progress when downloading large files, and Firefox's resumption issues have persisted for years. A practical workaround can help affected users avoid re-downloading gigabytes of data, while also highlighting gaps in browser download management. Resuming interrupted downloads generally depends on the server supporting HTTP Range requests, and one-time download links may still fail because the URL expires or changes. Community comments also point to Bugzilla bug 230870, opened in 2004, as evidence that this Firefox limitation is not new.

hackernews · speckx · Oct 12, 19:36 · [Discussion](https://news.ycombinator.com/item?id=50061791)

**Background**: HTTP Range requests, also called byte serving, let a client ask a server for only part of a file using the Range header. If the server supports it via Accept-Ranges, it responds with 206 Partial Content and a Content-Range header, which is what enables download managers to pause and resume. Firefox saves in-progress downloads as .part files, but its download manager has known limitations when a transfer is interrupted. External tools like aria2 and older programs such as GetRight are often used instead because they handle multi-connection and resumable downloads more reliably.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HTTP_Range_request">HTTP Range request</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Range_requests">HTTP range requests - MDN Web Docs</a></li>
<li><a href="https://blinksandbuttons.net/which-browser-can-resume-download/">Which Browser Can Resume Download ? - BlinksAndButtons</a></li>

</ul>
</details>

**Discussion**: Commenters share manual workarounds, such as moving the .part file, restarting the download, pausing, replacing the new .part file with the old one, and resuming. Many express frustration that Bugzilla bug 230870 has remained open since 2004, and several recommend using external download utilities like aria2 instead of browser downloads. Others add nostalgia for GetRight and note other long-broken Firefox features, such as the modal search highlight.

**Tags**: `#firefox`, `#browser`, `#downloads`, `#workarounds`, `#bugzilla`

---

<a id="item-13"></a>
## [Agent37 (YC F26) launches low-cost sandboxes for AI agents](https://news.ycombinator.com/item?id=50059096) ⭐️ 5.0/10

Agent37, a YC F26 startup founded by ex-Amazon engineer Vishnu, launched sandboxes for running AI agents at under 10% of the cost of most sandbox providers, with customers averaging $0.37 per sandbox per month and a newly added free plan. The company says its own infrastructure cost for free sandboxes runs about $0.05 to $0.10 per user per month. Agent sandboxes are a fast-growing but increasingly crowded infrastructure layer, and Agent37's price point tests whether aggressive cost optimization alone can win share against better-funded rivals. If the approach holds, it could pressure incumbent sandbox vendors on pricing and make always-on personal agents cheaper for individual developers. The cost savings come from four levers: exploiting the bursty CPU/RAM usage pattern of agent harnesses, renting bare-metal hosts from Hetzner and OVH instead of hyperscalers, using gVisor to share host memory across sandboxes without reserving a full VM per sandbox, and buying RAM-heavy host shapes. The tradeoff is that gVisor-based sandboxes cannot run workloads like Docker-in-Docker or Android emulators, so Agent37 also offers full VM sandboxes at a slightly higher price.

hackernews · vishnukool · Oct 12, 16:46

**Background**: An AI agent sandbox is an isolated runtime where an agent can execute code, browse the web, or perform computer-use tasks without touching the host system. A harness is the software scaffolding around a model — such as Claude Code or OpenClaw — that handles tool use, memory, and state so the model can act as an agent over many steps. Agent37 started in February as a wrapper around OpenClaw, an open-source personal AI agent that runs through chat apps, before expanding to support additional harnesses.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>
<li><a href="https://e2b.dev/">E2B | The Enterprise AI Agent Cloud</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly skeptical of the business rather than the technology: mparis and MikhailTal argued that sandboxes are commoditized, that competing purely on price invites a race to the bottom, and that hyperscalers with 80-90% VM margins could undercut Agent37 at a loss to protect stickier, higher-margin offerings. alasano gave a practical data point, saying Agent37 looks slightly cheaper than boat.dev but with less storage, while itissid criticized the launch's customer success stories as obviously Claude-written.

**Tags**: `#AI agents`, `#sandboxing`, `#startups`, `#cloud infrastructure`, `#Hacker News`

---

<a id="item-14"></a>
## [Citroën revives the iconic 2CV as a sub-tonne electric car](https://www.bbc.com/news/articles/c620r33plgppo) ⭐️ 5.0/10

Citroën has unveiled an electric revival of its iconic 2CV, a concept car that the company says weighs under a tonne, which would make it class-leading among modern EVs. The reveal has drawn substantial attention on Hacker News, where the discussion has focused as much on the engineering of its lightweight design as on the nostalgia of the original model. The announcement matters because lightweight engineering is a rare and increasingly valuable approach in an EV market where heavy battery packs dominate, since lower weight directly improves range, reduces tyre and road wear, and allows a smaller, cheaper battery. If the sub-tonne target survives into production, it could offer a template for affordable, efficient small EVs at a time when most new electric cars are getting larger and heavier. According to commenters, Citroën's official site and video show details such as an infotainment system cheekily named “Radioën”, distinctive “champignon” (mushroom) pedals, and a van variant, though the pedals may not survive production due to regulation and the seats will need headrests to meet modern safety rules. The car remains a concept, so its specifications, price target, and production viability are still unconfirmed.

hackernews · scrlk · Oct 12, 12:09 · [Discussion](https://news.ycombinator.com/item?id=50055220)

**Background**: The original Citroën 2CV was an economy car produced by the French automaker from 1948 to 1990, conceived by vice-president Pierre Boulanger to motorise rural French farmers who still relied on horses and carts. It became famous for minimalist, utilitarian engineering: an air-cooled engine driving the front wheels, long-travel suspension tuned to cross a ploughed field without breaking a basket of eggs, and a roll-back canvas roof. Over 3.8 million 2CVs were built, plus millions more of its A-Series derivatives, making it one of the best-selling and most beloved cars of the 20th century alongside the Volkswagen Beetle.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Citroën_2CV">Citroën 2CV</a></li>

</ul>
</details>

**Discussion**: Commenters largely welcomed the news: one noted that the nostalgic hype is overshadowing the genuinely class-leading sub-tonne weight, which enables better range from a smaller battery and lower road wear and is a key reason the car can be so cheap. Others praised the playful details like the “Radioën” infotainment and mushroom pedals, expressed appreciation for a car that “looks happy” amid a trend of aggressive-looking vehicles, and wondered whether the concept will ever reach production or be benchmarked against existing EV-converted 2CVs.

**Tags**: `#Electric Vehicles`, `#Automotive`, `#Design`, `#Lightweight Engineering`, `#Nostalgia`

---

<a id="item-15"></a>
## [Meta debuts Muse Wonder AI model behind a paid Muse subscription](https://www.cnbc.com/2026/10/12/meta-muse-wonder-ai-model-agent.html) ⭐️ 5.0/10

Meta introduced its Muse Wonder AI model, which users can only access through a paid subscription to the Muse app, according to a CNBC report published on October 12, 2026. Meta's own announcement describes Muse Wonder and Muse Wonder Full as its most capable models to date, built for personal and professional agentic tasks. The release turns Meta's newest frontier model into a paywalled product, making it a direct test of whether users accustomed to free social-media services will pay for AI access. It also signals that Meta is moving to monetize AI directly rather than relying solely on advertising, putting it in competition with paid tiers from other frontier labs. Meta's developer documentation says the Muse Wonder series combines frontier coding capabilities, long-running agents, and advanced computer use for demanding work. The models run alongside the Muse personal agent app, which Meta says runs on Muse Secure VM, a dedicated secure computer environment; pricing tiers and free-access limits were not detailed in the coverage.

rss · CNBC Top News · Oct 12, 17:34

**Background**: Meta launched the Muse app in September 2026 as a "personal AI agent" that can act on a user's behalf — for example sending emails or booking trips — echoing similar agent products from other AI companies. An "agentic" model is one designed not just to answer questions but to carry out multi-step tasks autonomously on a computer. Meta has historically earned nearly all of its revenue from advertising, so charging for AI access is a notable strategic shift, and the Muse Wonder models are positioned as Meta's competitor to leading frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/10/introducing-muse-wonder-models/">Introducing Muse Wonder and Muse Wonder Full: Frontier Models ...</a></li>
<li><a href="https://research.meta.ai/blog/muse-wonder">Muse Wonder | Meta AI Research</a></li>
<li><a href="https://dev.meta.ai/models/muse-wonder">Muse Wonder | Meta</a></li>

</ul>
</details>

**Tags**: `#Meta`, `#AI models`, `#subscription`, `#monetization`, `#Muse Wonder`

---

<a id="item-16"></a>
## [Intel, Broadcom CEOs Warn Capital Crunch Could Bottleneck AI Boom](https://www.cnbc.com/2026/10/12/intel-broadcom-ceos-warn-capital-crunch-could-become-ai-bottleneck.html) ⭐️ 5.0/10

The CEOs of Intel and Broadcom publicly warned that limited access to capital could emerge as a major constraint on the artificial intelligence boom, according to a CNBC report. The warning frames financing — not chips, power, or talent — as a potential limiting factor for continued AI expansion. The AI buildout is one of the most capital-intensive technology cycles in history, so any tightening in financing could ripple through data center construction, chip orders, and the valuations of suppliers and hyperscalers alike. Coming from two major semiconductor CEOs, the warning is a notable signal that industry leaders see funding — not just technical limits — as the next risk to AI growth. The report is a brief, headline-level item: it does not name which specific capital sources are constrained, quantify the shortfall, or cite figures such as capex totals or interest costs. It also does not specify whether the concern is about debt financing, equity markets, or internal cash flow at the chipmakers' customers.

rss · CNBC Top News · Oct 12, 13:04

**Background**: The current AI boom depends on enormous upfront spending on data centers, AI accelerators, networking gear, and electricity supply, much of which is funded through a mix of hyperscaler cash flow, debt, and increasingly complex financing arrangements. Intel is a long-established chipmaker with CPU and foundry businesses, while Broadcom supplies networking silicon and custom AI accelerators for large cloud customers, making both companies sensitive to how much their customers can afford to spend. When capital becomes harder or more expensive to obtain, infrastructure projects can be delayed or scaled back, which in turn reduces demand for the chips these firms sell.

**Tags**: `#AI infrastructure`, `#semiconductors`, `#industry news`, `#capital markets`, `#Intel/Broadcom`

---

<a id="item-17"></a>
## [UK AI minister warns cyber defences 'likely' to be breached](https://www.bbc.co.uk/news/articles/cr78pe09y05xo?at_medium=RSS&at_campaign=rss) ⭐️ 5.0/10

UK AI minister Kanishka Narayan said it is "likely" that the UK's cyber defences will be breached, and stated that the government will use advanced AI to strengthen the country against cyber attacks. The remark signals that a senior government figure now treats a successful major cyber intrusion as a matter of when rather than if, which shifts the policy debate from pure prevention toward resilience and AI-assisted detection. It also indicates that national governments are becoming major buyers and drivers of AI-based security tooling, a market that affects defence contractors, security vendors and critical-infrastructure operators. The announcement as reported is brief and does not specify funding figures, timelines, named AI systems, or which departments and agencies would lead the effort; the word "likely" itself frames breach prevention as an accepted risk rather than a guarantee. A technically minded reader should note that no technical mechanism, procurement route or threat model was disclosed, so the practical scope of the AI deployment remains unclear.

rss · BBC Business · Oct 12, 15:03

**Background**: Cyber defence is the practice of protecting networks, systems and data from intrusion, and governments typically handle it through national agencies that share threat intelligence with critical sectors such as energy, health and finance. AI is increasingly used on both sides of this contest: attackers can automate phishing, reconnaissance and vulnerability discovery, while defenders use machine learning for anomaly detection, log analysis and rapid incident triage. Because national cyber strategies are published as policy documents, ministerial statements like this one usually preview spending priorities, legislation or new agency responsibilities rather than announcing a finished technical product.

**Tags**: `#AI policy`, `#cybersecurity`, `#UK government`, `#national security`, `#AI defense`

---

