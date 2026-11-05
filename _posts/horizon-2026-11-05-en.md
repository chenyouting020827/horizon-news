# Horizon Daily - 2026-11-05

> From 162 items, 19 important content pieces were selected

---

1. [sshole: OpenSSH on musl libc accepts any long password for locked accounts](#item-1) ⭐️ 8.0/10
2. [Kagi Widens Access to Its Ad-Free, Subscription Search Engine](#item-2) ⭐️ 7.0/10
3. [Claude Code Reportedly Leaks User and Org Identifiers via User-Agent Headers](#item-3) ⭐️ 7.0/10
4. [Motorola Signature 27 becomes first non-Pixel phone with official GrapheneOS support](#item-4) ⭐️ 7.0/10
5. [Rivet launches open-source actor orchestrator for AI agents on S3](#item-5) ⭐️ 7.0/10
6. [Essay Argues Ad Targeting Still Misreads Users, Sparking HN Debate](#item-6) ⭐️ 7.0/10
7. [U.S. warns of 'ongoing cyber threat' to industrial refrigeration systems](#item-7) ⭐️ 7.0/10
8. [Hackintosh Reborn: Running macOS on Non-Apple Hardware With AI Help](#item-8) ⭐️ 6.0/10
9. [Tencent launches Hy4, claiming top-tier open-source AI model](#item-9) ⭐️ 6.0/10
10. [Servo's September Update Adds <progress> Element and Rounded Rectangles](#item-10) ⭐️ 6.0/10
11. [Essay Urges Users to Archive Their Favorite YouTube Videos Before They Vanish](#item-11) ⭐️ 6.0/10
12. [Bilateral Cochlear Implant User's Hearing Psychophysics Essay Draws Expert HN Commentary](#item-12) ⭐️ 6.0/10
13. [Tech Stocks Fall as US Midterms Raise AI and Data Center Scrutiny Fears](#item-13) ⭐️ 6.0/10
14. [UK MPs Warn of 'Dangerous' Reliance on China for Critical Minerals](#item-14) ⭐️ 6.0/10
15. [Salon, the Internet's Oldest General-Interest Publication, Shuts Down After 31 Years](#item-15) ⭐️ 6.0/10
16. [MS Paint RCE Flaw Patched Only via the Microsoft Store](#item-16) ⭐️ 5.0/10
17. [Democrats push national data center moratorium after midterm wins](#item-17) ⭐️ 5.0/10
18. [Over 100 groups in 15 countries to protest European datacentres](#item-18) ⭐️ 5.0/10
19. [Guardian warns Australia's AI datacentre boom could be political kryptonite](#item-19) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [sshole: OpenSSH on musl libc accepts any long password for locked accounts](https://sshhole.com/) ⭐️ 8.0/10

A vulnerability nicknamed "sshole" (CVE-2026-123158) was disclosed in OpenSSH: on Linux systems that use musl libc without PAM — most notably Alpine Linux — sshd accepts any password of roughly 257 to 1024 bytes for accounts whose shadow password field is "*", because musl's crypt() returns the single character "*" as a failure sentinel when the supplied password exceeds its 256-byte limit, and sshd's comparison of the returned value against the stored hash then succeeds. OpenSSH 10.6p2 has been released with a workaround, and Alpine has published fixed openssh packages. Any Alpine or other musl-based host, container image, or appliance that runs sshd and relies on "*" to lock password login can be accessed with a trivially crafted overly long password, silently defeating the common "key-only" hardening pattern. It is also a textbook example of why in-band signaling in security-critical APIs is dangerous, which matters far beyond this one bug. The flaw is limited to Linux systems using musl libc without PAM; glibc systems, PAM-based systems, and non-Linux platforms are not affected, and the vulnerable path in musl is only slightly exploitable depending on configuration. Upgrading the package alone is not enough — the running sshd daemon must be restarted — and as an interim mitigation administrators can set PasswordAuthentication=no or disable SSH access until OpenSSH 10.6p2 is applied.

hackernews · josemrb · Nov 5, 12:19 · [Discussion](https://news.ycombinator.com/item?id=50378228)

**Background**: Unix systems store password hashes in /etc/shadow, and the crypt() libc function is what sshd calls to hash a supplied password and compare the result with the stored value. By long-standing convention, a shadow field of "*" or "!" means the account has no usable password — it is intentionally not a valid hash, which is how administrators lock password login while still permitting SSH keys. In-band signaling is the practice of encoding control meaning inside the same value space as ordinary data (here, using a magic string instead of a separate error signal), which becomes dangerous when a consumer cannot distinguish "failure" from "valid value".

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/">OpenSSH flaw lets attackers log into password-disabled Linux ...</a></li>
<li><a href="https://hadrian.io/vulnerability-alerts/openssh-on-musl-accepts-any-long-password-for-locked-accounts">From * to Access: How musl’s crypt () Behavior Undermines ...</a></li>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh-server password ... | Alpine Linux</a></li>

</ul>
</details>

**Discussion**: Commenters quickly converged on the root cause: mpyne walked through how the attacker's goal is simply to make crypt($pw, $hash) return a value equal to the stored $hash, which is exactly what happens when the stored hash is "*" and crypt() fails. BoppreH and aljgz argued that "*" should never have been used as a sentinel in either /etc/passwd or crypt(), advocating explicit failure values or Result-like types over magic strings, while amluto noted that musl had already patched this class of failure in crypt_des but forgot crypt_sha — and that the existing workaround is itself wrong when the salt is "x".

**Tags**: `#security`, `#ssh`, `#cryptography`, `#vulnerabilities`, `#unix`

---

<a id="item-2"></a>
## [Kagi Widens Access to Its Ad-Free, Subscription Search Engine](https://kagi.com/changelog) ⭐️ 7.0/10

Kagi announced broader availability of its paid, ad-free search engine through a "Kagi Search for Everyone" changelog update, signaling it is opening the service to more users beyond its earlier invite/waitlist-limited rollout. The announcement drew a substantial Hacker News thread with 352 points and 183 comments debating pricing, custom ranking, and life after Google. It marks another step in the small but growing niche of paid, ad-free search, which inverts the ad-supported model of Google and DuckDuckGo by making users rather than advertisers the customer. Growth here matters most to privacy-conscious users and to developers whose AI agents depend on search APIs, since the economics of that access are still unsettled. Kagi's differentiators include user-adjustable result ranking (promoting or demoting entire domains), domain blocking, and AI summarization that only triggers when a query ends with a question mark rather than being forced on every search. A recurring complaint is that API usage for agents and automated search is billed separately from the subscription, effectively requiring some users to pay twice.

hackernews · elashri · Nov 5, 20:03 · [Discussion](https://news.ycombinator.com/item?id=50383740)

**Background**: Kagi is a paid, ad-free search engine developed by Kagi Inc., a company based in Palo Alto, California, and its name comes from the Japanese character 鍵 (kagi), meaning "key". Instead of monetizing attention through ads and tracking, it charges subscribers directly, and it offers its own index alongside results blended from other engines. It is part of a small wave of subscription search efforts — earlier entrants such as Neeva shut down — that also includes privacy-oriented players like DuckDuckGo, Ecosia and Qwant.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kagi_(search_engine)">Kagi (search engine)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kagi">Kagi - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Long-time subscribers praise the ability to downrank sites like Reddit or outright remove AI-generated listicles, and many say the ad-free, no-AI-by-default experience feels markedly better than ad-supported search. The sharpest criticism is directed at API pricing: one user argues that if their agents are searching the web on their behalf, that usage should be included in the plan with perhaps a soft cap rather than billed extra. Others remain on DuckDuckGo out of habit but are increasingly uneasy about not recognizing or trusting top results, while some former Kagi users switched to Ecosia to support European alternatives.

**Tags**: `#search-engines`, `#kagi`, `#privacy`, `#product-announcement`, `#hacker-news-discussion`

---

<a id="item-3"></a>
## [Claude Code Reportedly Leaks User and Org Identifiers via User-Agent Headers](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 7.0/10

A GitHub issue (#107757) and a Hacker News thread (141 points, 31 comments) report that Anthropic's Claude Code injects user and organization identifiers — including names, company/team names, GitHub org paths and in some cases email addresses — into HTTP User-Agent headers on outbound requests, especially when subagents run curl. Commenters posted header dumps such as "company-helm-research/1.0 (Claude Code agent run by <name>, <company> platform team; docs lookup)" and "Claude-Code-research-agent/1.0 (<Company> platform team; on behalf of <name>)". Because every server, proxy, CDN and logging pipeline that receives these requests can read the User-Agent string, users of a widely adopted AI coding tool may be silently exposing their identity and employer to arbitrary third-party sites, which commenters link to personally addressed spam. Anyone running Claude Code against external services — especially inside a corporate network — should audit their outbound headers immediately. The information appears to originate from agent-generated curl commands rather than every request: at least one user reported seeing only a generic "Claude-User (claude-code/2.1.318 (cli); +https://support.anthropic.com/)" header, while another said curl used their organization email address even when they were logged into a personal Claude account. Reports remain largely anecdotal — there is no confirmed root cause, version range, or statement from Anthropic, so the exact trigger and scope are still unclear.

hackernews · motoroco · Nov 5, 22:17 · [Discussion](https://news.ycombinator.com/item?id=50385272)

**Background**: The HTTP User-Agent header is a standard request header that tells a server which client application, version and platform is making the call; servers and logs routinely record it. Claude Code is Anthropic's agentic coding tool that runs in the terminal and IDE and can execute shell commands, including curl, on the user's behalf. Bot-identification conventions encourage automated clients to put a contact name or URL in the User-Agent so site operators can reach them — a practice that becomes a privacy leak when the 'contact' is the end user's real name and employer.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/User-Agent_header">User - Agent header - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent">User - Agent header - HTTP | MDN</a></li>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI coding agent and assistant</a></li>
<li><a href="https://everything.curl.dev/http/modify/user-agent.html">User-agent - everything curl</a></li>

</ul>
</details>

**Discussion**: Sentiment in the Hacker News thread is largely negative and alarmed: multiple users say they observed identifier-laden headers, and one reports a sharp rise in personalized work-email spam since switching from Copilot to Claude. The thread is not unanimous, however — at least one commenter sees only a generic Claude Code header and asks others what situation triggers the leak, leaving the scope disputed.

**Tags**: `#privacy`, `#security`, `#claude-code`, `#ai-tools`, `#user-agent`

---

<a id="item-4"></a>
## [Motorola Signature 27 becomes first non-Pixel phone with official GrapheneOS support](https://motorolanews.com/motorola-signature-27-2/) ⭐️ 7.0/10

Motorola's new Signature 27 flagship, priced at a $1,599 starting MSRP, is being promoted as the first non-Google device to receive official GrapheneOS support, after the GrapheneOS project announced in 2026 that it plans to certify selected Motorola devices. The phone ships with Motorola's own Android build and Gemini integration, but buyers will be able to install the privacy-hardened GrapheneOS as an officially supported option. Until now GrapheneOS has been effectively Pixel-exclusive because of its strict hardware security requirements, so certifying a second OEM meaningfully widens the pool of trusted mobile hardware for privacy-conscious users. It also signals that GrapheneOS is moving from a single-vendor niche project toward a broader platform that pressures other manufacturers on bootloader unlocking and long-term firmware support. GrapheneOS's support hinges on the device meeting its hardware security baseline, and commenters note that Motorola modifies large parts of the board support package — bootloader, modem and its "mot_sec" additions — which raises questions about whether Qualcomm and Motorola will let the project rebuild or audit those components. It is also unclear how many of the Signature 27's camera, audio, EVS and OIS features will survive on GrapheneOS, and at $1,599 the phone costs roughly ten times a used Pixel.

hackernews · monneyboi · Nov 5, 16:01 · [Discussion](https://news.ycombinator.com/item?id=50380810)

**Background**: GrapheneOS is an open-source, non-profit mobile operating system built on the Android Open Source Project that hardens Android with stricter sandboxing, permission controls and attack-surface reduction; it ships without Google services, though Play Store can be installed in a sandboxed profile. Because it relies on verified boot and vendor-provided firmware security guarantees, it has historically been supported only on Google Pixel devices released between 2021 and 2025. Firmware and bootloader components form a supply chain that the OS cannot replace on its own, which is why hardware vendor cooperation is a precondition for any new device being certified.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were broadly skeptical: some questioned trusting a Lenovo-owned Motorola given past affiliate-code injection incidents and its opaque firmware modifications, while others worried GrapheneOS would cripple the Signature 27's camera and audio features, making the $1,599 price hard to justify against a used Pixel. Several also found the pairing of GrapheneOS with promoted Gemini integration contradictory, and one commenter hoped the required hardware support would eventually trickle down to Motorola's mid-range phones.

**Tags**: `#GrapheneOS`, `#mobile security`, `#privacy`, `#Android`, `#Motorola`

---

<a id="item-5"></a>
## [Rivet launches open-source actor orchestrator for AI agents on S3](https://github.com/rivet-dev/rivet) ⭐️ 7.0/10

YC W23 startup Rivet launched an open-source, self-hostable actor-model orchestrator for agentic workloads, where each agent runs as a lightweight actor (72 KB baseline, 4.9 ms p99 cold start) with in-memory state, a WebSocket server, and durable SQLite storage backed by S3, instead of a heavyweight per-agent sandbox. The team reports 1.07 ms durable writes (3 AZ, p99), 1.36 ms cached reads, and 138 ms reads from object storage, with data stored 10× cheaper than on EBS gp3. Running every agent in its own sandbox is expensive, mostly idle, and slow to start, so an actor-based alternative that is both cheap and fast could reshape how agent infrastructure is built; Rivet positions itself as an open-source, self-hostable answer to Cloudflare Durable Objects, and at least one company (Amp) migrated off Durable Objects to Rivet in a weekend to deploy on-prem. The storage design is tiered rather than writing directly to S3: a write is acknowledged once SSDs in 2 of 3 availability zones have it, then batched to S3 in the background so object storage never sits on the write path, with SSD caches tunable to balance speed and cost. Self-hosting requires deploying a single Rust binary with S3 as the only dependency, and Rivet also offers dedicated cloud clusters on AWS or GCP plus BYOC deployment into a customer VPC.

hackernews · NathanFlurry · Nov 5, 17:17 · [Discussion](https://news.ycombinator.com/item?id=50381687)

**Background**: The actor model is a concurrency framework in which independent entities called actors hold their own state and communicate only through asynchronous messages, which makes it well suited to long-lived, stateful workloads such as AI agents. Cloudflare Durable Objects popularized this pattern as a hosted service, pairing each object with SQLite-backed storage, but it is proprietary and subject to platform limits. Rivet originally built infrastructure for multiplayer games and previously ran on FoundationDB before moving to S3, after customers began storing far more data (session transcripts, artifacts, whole filesystems) in actors than in Postgres.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/durable-objects/">Overview · Cloudflare Durable Objects docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Actor_model">Actor model - Wikipedia</a></li>
<li><a href="https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/">SQLite - backed Durable Object Storage · Cloudflare Durable Objects...</a></li>

</ul>
</details>

**Discussion**: Reception was positive and substantive: commenters said the explanation of keeping S3 off the write path made the storage model much easier to understand, and one reported migrating a Cloudflare Durable Object workload into their own VPC with a very pleasant experience. Others described frustration with Durable Objects' split agent tooling and limits, saying Rivet's S3 setup looks like a closer fit for their next project, while one person flagged a broken README link on GitHub.

**Tags**: `#ai-agents`, `#actor-model`, `#distributed-systems`, `#open-source`, `#durable-objects`

---

<a id="item-6"></a>
## [Essay Argues Ad Targeting Still Misreads Users, Sparking HN Debate](https://rakhim.exotext.com/i-wish-tech-companies-knew-more-about-me) ⭐️ 7.0/10

A blog post on rakhim.exotext.com titled "I wish tech companies knew more about me" argues that despite massive data collection, tech companies' personalization and ad-targeting systems still fail to understand basic user preferences. The piece reached the front page of Hacker News and drew roughly 238 comments debating privacy, adtech incentives, and the limits of recommendation algorithms. The discussion cuts to a core tension of the ad-funded web: more surveillance does not automatically produce better recommendations or ads, which undermines a common justification for pervasive tracking. It matters to anyone who uses ad-supported platforms, and to regulators and engineers weighing whether data collection actually serves users or mainly serves advertisers' incentives. Commenters noted concrete failures, such as recommendation systems on Spotify and YouTube Music never noticing that a user skips every electronic track with vocals, and argued that what gets promoted is often driven by who pays rather than by genuine preference modeling. Others contended that targeted advertising cannot feel good even with perfect data, since advertisers are trying to sell their own products rather than find what a user actually wants.

hackernews · freetonik · Nov 5, 13:40 · [Discussion](https://news.ycombinator.com/item?id=50378942)

**Background**: Adtech (advertising technology) is the infrastructure that buys, sells, and targets digital ad inventory, typically through real-time bidding, using tracking data about which sites and pages a user visits. Personalization and recommendation systems build on similar behavioral signals to predict what content or products a user will engage with. Critics argue both rely on proxy signals that capture clicks and exposure rather than a user's actual intent, so collecting more data does not necessarily improve the result and raises privacy and transparency concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2407.18937">Advancements in Recommender Systems: A Comprehensive Analysis ...</a></li>
<li><a href="https://bppblog.com/2025/09/02/algorithms-autonomy-recommender-systems/">Algorithms and Autonomy: Regulating Recommender Systems</a></li>
<li><a href="https://thecmo.com/marketing-operations/martech-vs-adtech/">MarTech vs. AdTech : 4 Key Differences Explained</a></li>

</ul>
</details>

**Discussion**: Sentiment was broadly skeptical of adtech: one commenter argued Google's real proposition is selling advertisers the audience of an expensive site like the New York Times on a cheaper site, making intent understanding secondary to tracking. Others said they would happily fill out an explicit purchasing-intent form instead of being passively tracked, while another described disabling an ad blocker on the BBC and being glad not to browse the web that way.

**Tags**: `#personalization`, `#adtech`, `#privacy`, `#recommendation-systems`, `#hacker-news-discussion`

---

<a id="item-7"></a>
## [U.S. warns of 'ongoing cyber threat' to industrial refrigeration systems](https://www.cnbc.com/2026/11/05/us-warns-of-ongoing-cyber-threat-to-industrial-refrigeration-systems.html) ⭐️ 7.0/10

U.S. authorities issued a warning about an "ongoing cyber threat" to commercial and industrial refrigeration systems, saying at least three distinct waves of attacks have hit commercial fridges and freezers in recent months. Refrigeration controllers are operational technology that directly governs food storage temperatures, so a successful hack can spoil inventory, disrupt a retailer's food supply chain and create food-safety risks — the same equipment families are deployed in supermarkets, hospitals and cold storage worldwide, meaning the threat is not confined to one country. The warning follows an earlier wave in which internet-exposed refrigeration controllers — reportedly Danfoss units running web servers reachable from the public internet, many with trivial credentials such as the username "admin" and the current date as the password — were manipulated remotely; the latest U.S. advisory itself is light on technical indicators, and no group has claimed responsibility for the attacks.

rss · CNBC Top News · Nov 5, 19:26

**Background**: Operational technology (OT) security covers the industrial control systems that run physical processes — in this case the controllers that let operators remotely monitor refrigeration units, adjust temperatures and perform maintenance, often from a single management platform spanning many units. Because these devices are increasingly connected to the internet for remote management, poorly secured controllers become attractive targets. A cyberattack in October 2026 forced major French retailers to throw away food after hundreds of store refrigeration systems were hit, an incident described as the first cyberattack with a real-world effect on a nation's food supply chain.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_French_supermarket_refrigerator_hack">2026 French supermarket refrigerator hack - Wikipedia</a></li>
<li><a href="https://english.news.cn/20261104/1b121d31e17b4f03889be8c1c590ac39/c.html">Europe's supermarket fridges hit by cyberattack : what is at risk?-Xinhua</a></li>
<li><a href="https://www.cisco.com/site/us/en/learn/topics/security/what-is-ot-security.html">OT security: protect ICS and infrastructure [Explained] - Cisco</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#IoT security`, `#OT security`, `#industrial control systems`, `#critical infrastructure`

---

<a id="item-8"></a>
## [Hackintosh Reborn: Running macOS on Non-Apple Hardware With AI Help](https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/) ⭐️ 6.0/10

A blog post published on November 5, 2026 at naut.ca revisits the Hackintosh — the practice of running macOS on non-Apple hardware — this time rebuilt with AI assistance, roughly a decade after the author's earlier guide for running macOS 10.14 inside a VM on an x86 host. The post triggered a Hacker News thread with 155 points and 61 comments debating Apple hardware, Linux support, and the decline of x86. Hackintosh has been widely considered a dying hobby since Apple completed its transition to Apple Silicon, which closed off the x86 path that nearly all Hackintosh guides depended on. The renewed interest shows that demand for macOS-compatible hardware alternatives — and for the reverse, Linux on Apple's excellent laptops — remains strong even as the technical window narrows. Modern Hackintosh setups revolve around the OpenCore bootloader, which injects SMBIOS data, ACPI tables and kernel extensions (kexts) such as Lilu and WhateverGreen via a config.plist, and AI tools are now being used to generate or tune that configuration for specific hardware. The approach still cannot overcome hardware-level barriers such as locked bootloaders on iPhones and iPads, and Apple Silicon Macs require entirely different work like the Asahi Linux project rather than macOS-on-generic-PC patching.

hackernews · rubatuga · Nov 5, 19:08 · [Discussion](https://news.ycombinator.com/item?id=50383057)

**Background**: A "Hackintosh" is a non-Apple PC modified to run Apple's macOS, a practice dating back to the late 1980s and made practical in the mid-2000s when hobbyists found ways to install retail copies of Mac OS X on generic Intel hardware. Getting it to work requires emulating what a real Mac's firmware provides: a bootloader (historically Clover or Chameleon, now OpenCore) fakes the machine identity, patches ACPI tables, and loads drivers Apple never intended to run on that hardware. Apple's move from Intel x86 chips to its own ARM-based Apple Silicon starting in 2020, combined with macOS dropping x86 support, made the classic approach far harder — which is why hobbyists are looking at AI-assisted configuration to lower the trial-and-error burden.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hackintosh">Hackintosh - Wikipedia</a></li>
<li><a href="https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/">The Hackintosh Reborn... with AI - naut.ca</a></li>
<li><a href="https://github.com/acidanthera/OpenCorePkg">GitHub - acidanthera/OpenCorePkg: OpenCore bootloader</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed that Apple's advantage now lies in hardware rather than software, with several saying they would happily run Linux on a MacBook if they could and hoping Asahi Linux eventually supports the M5. Others lamented that locked iDevice bootloaders mean there is still no macOS on iPad, and one noted that ARM-based Macs running Switch games natively feels like a first-hand sign of the end of x86.

**Tags**: `#hackintosh`, `#macOS`, `#Apple hardware`, `#Linux`, `#ARM`

---

<a id="item-9"></a>
## [Tencent launches Hy4, claiming top-tier open-source AI model](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/) ⭐️ 6.0/10

Tencent announced Tencent Hy4, its latest-generation large language model, saying it represents a significant leap in performance and now ranks among the world's leading open-source AI models. Tencent Hy plans to release the model weights and system cards in the coming days, following the earlier open-source release of Hy4 preview. A credible top-tier open-weight model from a major Chinese platform expands the choices available to developers who want strong models without vendor lock-in or API dependence. It also intensifies competition among Chinese labs racing to ship leading open-source models, which increasingly sets the pace for the global open-weight ecosystem. Tencent says Hy4 scores 12.03 percentage points higher than Hy4 preview on IRAB, an internal benchmark from financial AI agent company RabyteTech, and that search was upgraded for time-sensitive retrieval, multi-source synthesis and factual consistency verification to suit financial and office workflows. Notably, the weights themselves were not yet available at announcement time, so independent verification of the claimed gains is still pending.

hackernews · gmays · Nov 5, 20:21 · [Discussion](https://news.ycombinator.com/item?id=50383963)

**Background**: Tencent Hy is Tencent's large language model family; an earlier "Hy4 preview" release was open-sourced with a big expansion in model size, context length and training data. "Open-source" (more precisely open-weight) models let anyone download the parameters and run or fine-tune them locally, in contrast to closed models accessible only through an API. Benchmarks like IRAB are internal evaluation sets, so scores are self-reported and not directly comparable across vendors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/">Tencent Launches Hy4, Joining the Ranks of the World's ...</a></li>
<li><a href="https://hy.tencent.ai/research/hy4">Tencent Hy</a></li>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open-Sources Tencent Hy4 preview</a></li>

</ul>
</details>

**Discussion**: Discussion was essentially absent: the only comment simply flags the submission as a duplicate and links to another Hacker News thread on the same story. No substantive technical opinions, praise or criticism were expressed.

**Tags**: `#AI`, `#open-source`, `#Tencent`, `#LLM`, `#model-release`

---

<a id="item-10"></a>
## [Servo's September Update Adds <progress> Element and Rounded Rectangles](https://servo.org/blog/2026/11/05/september-in-servo/) ⭐️ 6.0/10

Servo published its September monthly progress report, highlighting newly implemented web-platform features including the HTML <progress> element and rounded rectangles (CSS border-radius), built on top of roughly 527 commits during the month. The post also covers assorted engine fixes and improvements, with commenters noting that basic features like :checked were only recently supported. Each of these additions closes a gap that previously kept real-world sites from rendering correctly in Servo, which matters for anyone hoping for a credible non-Chromium engine in Rust for browsers, embedded webviews, and mobile apps. The contrast with Chromium's roughly 20,000 monthly commits also fuels an ongoing debate about whether a largely volunteer-driven engine can stay competitive. The report tallies 527 commits for the month, a fraction of Chromium's output, and community members note that the features shipped here are long-standing basics in mainstream browsers. Servo also offers a breadth of pre-built release binaries, which commenters say makes day-to-day use considerably more practical, particularly on Android.

hackernews · iamnothere · Nov 5, 14:34 · [Discussion](https://news.ycombinator.com/item?id=50379576)

**Background**: Servo is an experimental browser engine written in Rust, originally started at Mozilla and now developed as an independent open-source project, designed to exploit Rust's memory safety and concurrency features. The <progress> element is a standard HTML tag that displays a bar showing completion of a task, while border-radius is the CSS property that rounds an element's corners. Both are extremely common on the modern web, so their absence means many pages render oddly or not at all. Because Servo builds rendering from scratch, even well-established platform features must be implemented and tested one by one.

<details><summary>References</summary>
<ul>
<li><a href="https://servo.org/">Servo aims to empower developers with a lightweight...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Servo_(software)">Servo (software) - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress">HTML progress indicator element - HTML | MDN Usage example</a></li>

</ul>
</details>

**Discussion**: Commenters broadly admire Servo's clean, performance-focused Rust design and the dedication of largely unpaid contributors, but many doubt that occasional volunteer work can close the gap with Chromium. A developer building a progress-bar-heavy incremental game reported that Firefox renders it smoothly while Chrome stutters, skips paints, and delays animation frames, prompting hopes of testing Servo. Others pointed to the easy sponsorship route and the wide range of pre-built releases, especially on Android, as practical reasons for optimism.

**Tags**: `#servo`, `#browser-engine`, `#rust`, `#web-standards`, `#open-source`

---

<a id="item-11"></a>
## [Essay Urges Users to Archive Their Favorite YouTube Videos Before They Vanish](https://criminallyvulgar.dev/you-should-absolutely-download-your-favourite-youtube-videos/) ⭐️ 6.0/10

A post on criminallyvulgar.dev argues that anyone who values specific YouTube videos should download and keep local copies rather than trusting the platform to keep them online, and the piece sparked a Hacker News discussion that reached 248 points and 111 comments. The thread quickly moved from the basic advice to concrete loss rates, legal obstacles and yt-dlp command-line recipes for preserving playlist structure. Commenters report that roughly 10% of the videos in a five-year-old playlist are already unavailable, meaning personal media collections and the cultural record decay steadily through takedowns, deletions and channel closures. The discussion highlights a gap between individual archiving and public preservation: even people sitting on terabytes of saved video have no legal way to share it, so the material is effectively private-only. One commenter notes that yt-dlp alone can preserve playlist ordering with `--embed-metadata --parse-metadata "playlist_index:%(track_number)s"`, avoiding the need for wrappers such as ytdl-sub, while yt-dlp's `--download-archive` option prevents re-downloading files already saved. The caveat raised is that downloading only solves the private-copy problem, not the redistribution problem, and some users worry that publicizing archiving tricks (such as YouTube RSS feeds) could prompt YouTube to close those access paths.

hackernews · surprisetalk · Nov 5, 13:00 · [Discussion](https://news.ycombinator.com/item?id=50378571)

**Background**: yt-dlp is a community-maintained fork of youtube-dl, a free and open-source command-line downloader for YouTube and over a thousand other video sites; it is known for faster multi-threaded downloads, richer format selection and subtitle embedding, and it has replaced youtube-dl in several Linux distributions. Both tools have faced DMCA takedown notices and controversy over downloading copyrighted material, though they remain widely used for education, archiving, journalism and fair use. The phenomenon at the heart of the article is link rot: hyperlinks tend over time to stop resolving because the target has moved or become permanently unavailable, and information professionals warn that it can erase important archival data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yt-dlp">Yt-dlp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Link_rot">Link rot</a></li>
<li><a href="https://github.com/yt-dlp/yt-dlp/issues/2754">What can --download-archive be used for? · Issue #2754 · yt ...</a></li>

</ul>
</details>

**Discussion**: Sentiment is broadly supportive of archiving but split on what it achieves: several commenters share large personal archives yet lament that copyright rules make sharing impossible, so the data "goes to the grave" with them. Others push back on the hoarding instinct — one argues people should simply let things die and half-remembered media fade — while one archivist jokes that such advice should be kept quiet so YouTube does not take away RSS feeds and other access methods.

**Tags**: `#digital-preservation`, `#youtube`, `#yt-dlp`, `#copyright`, `#data-hoarding`

---

<a id="item-12"></a>
## [Bilateral Cochlear Implant User's Hearing Psychophysics Essay Draws Expert HN Commentary](https://claude.ai/artifact/L8qsMc3SorytGW3LA81nYf) ⭐️ 6.0/10

A bilateral cochlear implant (CI) user published a first-person account of the psychophysics of their own hearing — describing what sound, speech and music actually feel like through electrical stimulation — and the essay was shared on Hacker News, where it drew a substantive comment thread. That thread included an ENT surgeon who is himself a bilateral CI user with more than 20 years in CI research, plus readers probing apparent contradictions in the author's hearing history. First-person psychophysical reports from implant users are rare and give engineers, clinicians and would-be designers a ground-level view of where current CI speech and music processing strategies succeed and fail. The presence of a long-time CI researcher in the thread adds candid context about hard limits at the auditory nerve interface, which helps explain why many promising strategies never reach clinical use. The author notes they were born with normal hearing, began losing it in childhood, was fitted with hearing aids that made voices clear for a few months, and later hesitated over the cost of cochlear implant surgery before receiving bilateral implants — a sequence some commenters found confusing. All of the underlying data is published in a public GitHub repository (mi-rae-lab/ci-psychophysics-data), and the ENT surgeon in the thread observed that many key findings about the auditory nerve interface date from the 1960s–1990s and remain valid, with strategies that help some individuals but not enough to justify clinical rollout.

hackernews · mi-rae · Nov 5, 16:21 · [Discussion](https://news.ycombinator.com/item?id=50381033)

**Background**: Psychophysics is the study of the quantitative relationship between physical stimuli (such as sound pressure) and subjective perception; its auditory branch, psychoacoustics, examines how the human auditory system extracts features for speech recognition, sound localization and music. Cochlear implants bypass damaged hair cells by using processing strategies that translate incoming acoustic signals into electrical pulses delivered to auditory nerve fibers, and bilateral implantation (one device per ear) aims to restore some of the binaural cues used for localization and hearing in noise. Because the electrode array stimulates a small number of discrete sites rather than thousands of hair cells, pitch and timbre resolution is coarse, which is why music perception and speech-in-noise performance remain the field's hardest problems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Psychophysics">Psychophysics - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Psychoacoustics">Psychoacoustics - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4236803/">An Undecimated Wavelet-based Method for Cochlear Implant Speech ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely responded with curiosity and appreciation, though several pushed back on specifics: one questioned the framing of hearing a voice as feeling "vibrations" rather than a distinct auditory experience, and another was confused by the author's account of normal birth hearing, childhood hearing loss, hearing aids and then costly CI surgery. The most notable contribution came from an ENT surgeon and bilateral CI user with 20+ years in the field, who said improvements are constrained by the auditory nerve interface and that many effective strategies only work at the individual level. Others linked the project's open data repository and wondered whether real-time voice-transformation software like Voicemod could make speech easier to understand.

**Tags**: `#audiology`, `#cochlear-implants`, `#psychophysics`, `#human-computer-interface`, `#science`

---

<a id="item-13"></a>
## [Tech Stocks Fall as US Midterms Raise AI and Data Center Scrutiny Fears](https://www.bbc.co.uk/news/articles/cmn04705rd8jo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

Major US technology stocks fell after the US midterm election results heightened investor fears that data center construction and the AI industry could face tougher scrutiny. The sell-off reflects a market reaction to the possibility of tighter oversight rather than to any specific new rule announced so far. The AI boom has been powered largely by enormous capital spending on data centers, so any signal that permitting, power access, or oversight could tighten directly threatens the growth assumptions behind chipmakers' and hyperscalers' valuations. Because those valuations now rest on multi-year AI infrastructure buildouts, political risk in the US can move the entire global AI supply chain, from chip designers to cloud operators. The report is a brief market-reaction piece and does not specify the size of the declines or which companies were hit hardest, so the scale of the move remains unclear. Notably, the concern is less about federal AI legislation than about state and local authority over data center siting, grid hookups, and water use — decisions that voters and local officials influence most directly.

rss · BBC Business · Nov 5, 22:13

**Background**: US midterm elections determine control of Congress and also reshape statehouses, governorships, and local offices — the levels where many decisions about land use, electricity tariffs, and utility approvals are actually made. AI data centers consume very large amounts of electricity and water, and have already encountered local opposition and grid capacity constraints in several regions. As a result, tech valuations have become sensitive to any political signal that this infrastructure buildout could slow down.

**Tags**: `#AI industry`, `#tech stocks`, `#US midterms`, `#data centers`, `#regulation`

---

<a id="item-14"></a>
## [UK MPs Warn of 'Dangerous' Reliance on China for Critical Minerals](https://www.theguardian.com/world/2026/nov/05/uk-dangerously-reliant-on-china-critical-minerals-military-ai-renewable-energy) ⭐️ 6.0/10

A UK parliamentary committee investigation found that the country is "dangerously" dependent on China for the critical raw materials needed for the military, renewable energy infrastructure and AI, and the MPs called for an urgent centralised policy. The business select committee also proposed creating a "critical minerals finance facility" that would deploy grants, equity and debt to fund rare earth and other critical mineral mines and accelerate a diversification programme. Rare earths and other critical minerals underpin the permanent magnets in wind turbines and EVs, as well as defence systems and AI hardware, so depending on a single supplier gives China leverage over strategic UK industries. The committee warns that the net zero transition itself is at risk, placing the UK alongside the US and EU in a widening push to reshore and diversify supply chains. The recommendations come from the business select committee and are advisory rather than binding, so no funding or legislation has yet been committed. The proposed facility would blend grants, equity and debt — an implicit acknowledgment that private capital alone has not financed new mining and refining capacity — and because the UK has limited domestic deposits, diversification will largely mean sourcing from allies such as Australia, the US and Brazil.

rss · The Guardian Business · Nov 5, 05:00

**Background**: Rare earths are 17 metallic elements — the 15 lanthanides plus scandium and yttrium — used in high-strength permanent magnets, catalysts, lasers and electronics; despite the name they are relatively abundant in the crust but occur thinly dispersed and are costly and energy-intensive to separate and refine. China supplies roughly 90% of global rare-earth demand and dominates refining, and has restricted exports at various points since around 2010, with tighter controls after the 2025 trade war escalation. "Critical minerals" is a broader policy category for materials deemed essential to a country's economy or national security and exposed to supply risk, and the exact list differs by country. The UK has essentially no rare-earth production of its own, so it imports nearly all the material used in defence electronics, wind turbine generators and data-centre hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rare-earth_element">Rare-earth element</a></li>
<li><a href="https://www.usgs.gov/programs/mineral-resources-program/science/what-are-critical-minerals-0">What are Critical Minerals? | U.S. Geological Survey - USGS.gov</a></li>

</ul>
</details>

**Tags**: `#critical-minerals`, `#supply-chain`, `#geopolitics`, `#AI-infrastructure`, `#rare-earths`

---

<a id="item-15"></a>
## [Salon, the Internet's Oldest General-Interest Publication, Shuts Down After 31 Years](https://www.theguardian.com/media/2026/nov/05/salon-website-shuts-down) ⭐️ 6.0/10

Salon announced on Thursday, November 5, 2026, that it is shutting down after more than three decades of publishing, just weeks before its 31st anniversary. In a farewell statement titled "Goodbye from Salon," the outlet described itself as "an idea about what journalism could be, born at a moment when the internet was still a largely unexplored frontier." Salon was among the first publications built natively for the web, so its closure marks the end of one of digital journalism's founding experiments and a symbolic milestone in the long contraction of online media. It also highlights how the outlets that pioneered the open web are now being squeezed by platform traffic shifts and AI-generated search results. Salon launched in November 1995, founded by journalist David Talbot — formerly arts and features editor at the San Francisco Examiner — in the wake of the 1994 San Francisco newspaper strike, and originally ran on domains such as salon1999.com and salonmag.com. It built its reputation on politics, arts and culture coverage, long-form journalism and opinion rather than breaking news.

rss · The Guardian World · Nov 5, 21:27

**Background**: Before blogging, social media and the modern news feed existed, a handful of digital-only magazines tried to invent journalism for the web. Salon, founded in 1995 as a digital magazine covering books, culture and ideas, was one of the most prominent of these pioneers and survived the dot-com boom and bust. For readers of the 1990s web, it sat alongside sites like Suck.com as an emblem of a smaller, more text-driven and more cynical internet.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Salon_(website)">Salon (website) - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/11/05/business/media/salon-online-magazine-shutters.html">Salon, a Pioneer of Digital Journalism, Shuts Down - The New ...</a></li>
<li><a href="https://grokipedia.com/page/Salon.com">Salon.com — Grokipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely nostalgic, recalling early Salon writers such as Anne Lamott and describing the 1990s web as less clickbait-driven and more Gen X cynical. Several argued the decline predates AI and the open web's erosion: one commenter noted newsroom jobs fell 60% between 2008 and 2020, mostly wiping out beat reporters, foreign and statehouse bureaus, and specialty coverage, leaving fewer but more national news sources. Others said Salon had already lost its edge years ago, and one dismissed its recent relevance as traffic from astroturfed subreddits that dried up after Google's AI Overview reduced Reddit referrals.

**Tags**: `#media`, `#digital-publishing`, `#internet-history`, `#journalism`, `#business-news`

---

<a id="item-16"></a>
## [MS Paint RCE Flaw Patched Only via the Microsoft Store](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 5.0/10

Microsoft's modern Store version of MS Paint is affected by a remote code execution vulnerability tracked as CVE-2026-83844, covering versions from 11.0.0.0 up to (but not including) 11.2605.91.0. The fix ships only as a Microsoft Store app update rather than through Windows Update, so users who never open the Store may remain unpatched. It highlights a growing patching blind spot: as more inbox Windows components are decoupled from the OS and serviced through the Store, security fixes no longer arrive automatically with monthly Patch Tuesday updates. Because RCE bugs let an attacker run arbitrary code, even a low-privilege consumer app like Paint can serve as an entry point, and enterprises that block or ignore the Store may silently carry unpatched software. The advisory states that only Paint versions 11.0.0.0 through 11.2605.91.0 are vulnerable, so very old builds such as the XP-era mspaint.exe copied by some users are outside the affected range, though such unsupported binaries carry their own risks. Some reports cite a fixed build of 11.2609.401.0, so users should simply verify they are on the newest Store version rather than matching an exact number, and the advisory gives no technical detail on the attack vector.

hackernews · kuberwastaken · Nov 5, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50384233)

**Background**: Remote code execution (RCE) is a class of vulnerability that lets an attacker run their own code on someone else's machine, typically by tricking a victim into opening a crafted file or data — which is why image-viewing and editing apps are a classic target. Since spring 2021, Microsoft has shipped Paint as a Store-updated app that evolves separately from Windows, meaning its updates bypass the traditional Windows Update and Patch Tuesday pipeline. That separation speeds up feature delivery but also means users and IT admins must remember to check the Store for security fixes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.free-codecs.com/news/windows-11-paint-has-a-remote-hacking-bug-how-to-check-your-version-and-get-the-fix.htm">Windows 11 Paint Security Bug: How to Check and Get the Fix</a></li>
<li><a href="https://techora.ru/news/v-paint-dlya-windows-11-nashli-2026-11-05">В Paint для Windows 11 нашли опасную уязвимость, патч не...</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/remote-code-execution/">What is Remote Code Execution (RCE)? | CrowdStrike</a></li>

</ul>
</details>

**Discussion**: Commenters were mostly amused rather than alarmed: several noted they still run the old XP-era mspaint.exe and calc.exe, and one joked about awaiting a Raymond Chen write-up on the bug. A practical complaint stood out — Windows Update surfaced nothing, forcing users to fetch the fix from the Microsoft Store themselves — while others clarified that only Paint 11.0.0.0 up to 11.2605.91.0 is affected, so much older builds are likely safe.

**Tags**: `#security`, `#vulnerability`, `#windows`, `#microsoft`, `#cve`

---

<a id="item-17"></a>
## [Democrats push national data center moratorium after midterm wins](https://www.cnbc.com/2026/11/05/democrats-data-center-restrictions-midterms.html) ⭐️ 5.0/10

After the 2026 midterm elections, Democratic winners and progressive lawmakers are calling for stricter limits on AI development and data center construction, with some explicitly demanding a "national data center moratorium now." The push follows an election cycle in which voter concern over AI — particularly its energy and water footprint — became a visible political issue. The stance signals that AI infrastructure is shifting from an engineering and capex story into a partisan political fight, putting proposed multi-billion-dollar data center projects, utility planning and grid buildout at risk of delay in jurisdictions controlled by Democrats. It also raises the prospect of a patchwork of state and local restrictions that hyperscalers and chipmakers would have to navigate project by project. The calls are so far political signals rather than enacted law, though a federal "AI Data Center Moratorium Act" has been proposed that would impose a nationwide, conditional pause on building or upgrading AI data centers. Outside analyses argue the moratorium debate is inseparable from energy policy, since soaring data center demand has already driven a surge in new natural gas generation.

rss · CNBC Top News · Nov 5, 20:17

**Background**: AI data centers are warehouses of GPU servers that train and serve models, and they draw large amounts of electricity and water: nearly all the electrical power they consume becomes heat that must be removed, often via evaporative cooling. Communities in water-scarce regions have started to question how much power and water they are effectively giving up, and the debate has moved from technical forums into election politics. A moratorium would be a far more blunt instrument than the ratepayer protections and community-input pledges some AI companies have recently proposed.

<details><summary>References</summary>
<ul>
<li><a href="https://regulations.ai/regulations/RAI-US-NA-S421400-2026">AI Data Center Moratorium Act - United States</a></li>
<li><a href="https://www.eli.org/sites/default/files/files-pdf/56.Data_Center_Moratorium.pdf">A CALL FOR A NATIONAL DATA CENTER MORATORIUM AND POLICY FRAMEWORK</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/ai-data-center-what-to-know/">AI Data Centers : What to Know About Their Water and Energy Use</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#data centers`, `#regulation`, `#politics`, `#energy infrastructure`

---

<a id="item-18"></a>
## [Over 100 groups in 15 countries to protest European datacentres](https://www.theguardian.com/world/2026/nov/05/activists-across-europe-protests-ai-against-datacentres) ⭐️ 5.0/10

More than 100 campaign groups across 15 European countries are staging two days of action on 6–7 November 2026 under the "Stop Dirty Data Centres" banner, demanding a moratorium on large-scale AI datacentre projects. Planned actions include demonstrations outside the Polish parliament in Warsaw, in Dublin, outside a Microsoft facility in Denmark, in Amsterdam, and on London's Brick Lane. This is one of the first coordinated, multi-country expressions of public opposition to AI infrastructure buildouts in Europe, and it lands as grid connections, zoning and water use already delay projects in hubs such as Dublin, Frankfurt and Aragon. If the movement grows, it could translate into permitting risk and political pressure that raises costs or slows timelines for hyperscalers and the AI systems that depend on them. The campaign's central demand is an immediate moratorium on large projects, justified by environmental and social costs that organisers say "we can no longer afford"; actions are described as peaceful protests, meetings and speaker-led events rather than a single march. The coalition includes environmental groups such as the Green Web Foundation, which frames the issue around local community consent and democratic accountability rather than AI capability itself.

rss · The Guardian Business · Nov 5, 09:00

**Background**: Datacentres are the physical substrate of AI: training and serving large models requires dense compute, which in turn requires large amounts of electricity and, for cooling, water. As AI demand has surged, operators have raced to secure grid connections and land, drawing pushback over strained local power grids, water consumption and land use in regions such as Ireland, the Netherlands, Germany and Spain. The protests follow warnings reported in October 2026 that AI companies told UK ministers they had roughly a year to head off public opposition before construction could be threatened.

<details><summary>References</summary>
<ul>
<li><a href="https://stopdirtydatacentres.eu/">Stop Dirty Data Centres - Days of Action 6-7 Nov 2026</a></li>
<li><a href="https://www.thegreenwebfoundation.org/news/stop-dirty-data-centres-days-of-action-6-7-nov-2026/">Stop Dirty Data Centres days of action 6 & 7 Nov 2026</a></li>
<li><a href="https://aiineurope.co/sectors/europe-datacentre-quandary-demand-protests-deepdive-2026-05-26">Europe 's Datacentre Quandary Pits AI Demand… | AI in Europe</a></li>

</ul>
</details>

**Tags**: `#datacentres`, `#AI infrastructure`, `#energy/environment`, `#tech policy`, `#activism`

---

<a id="item-19"></a>
## [Guardian warns Australia's AI datacentre boom could be political kryptonite](https://www.theguardian.com/australia-news/2026/nov/06/ai-datacentre-boom-could-be-political-kryptonite-australia) ⭐️ 5.0/10

A Guardian Australia opinion piece published on 6 November 2026 argues that Prime Minister Anthony Albanese has yet to show ordinary voters any tangible benefit from the country's AI and datacentre boom, while the costs keep piling up. The article points to the Reserve Bank of Australia's assessment this week that datacentres are contributing to "inflationary pressures," made as the RBA lifted interest rates to an 18-year high. The piece argues that without visible consumer benefits, the AI build-out could shift from an economic talking point into an electoral liability, citing the US midterms as evidence that public skepticism about AI and datacentres can be politically damaging. The framing matters for Australian policymakers, datacentre operators and energy planners, since planning approvals and power-and-water arrangements increasingly depend on local public consent. The article lists what Australians have seen so far as mostly costs: proposed copyright changes that would hurt Australian creatives, special rules governing datacentre power and water use, the threat of mass worker displacement, and — as it wryly puts it — a "mere 10% chance of human extinction" cited by an Anthropic researcher. It is an opinion and political analysis piece rather than a technical report, so it offers no new data or technical detail on datacentre capacity or investment figures.

rss · The Guardian World · Nov 5, 14:00

**Background**: Australia has attracted a wave of AI datacentre investment, and AI-focused facilities can draw three to five times more power per square foot than traditional datacentres, alongside significant water use for cooling — which puts them in direct tension with electricity prices and local resources. Separately, Australia's law reform bodies have floated copyright changes such as a text-and-data-mining exception to accommodate AI training, a debate that has alarmed authors and other creatives. The RBA's decision to raise rates to an 18-year high amid inflation concerns gives critics a concrete pocketbook argument against rapid datacentre expansion.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnet.com/tech/services-and-software/ai-data-center-what-to-know/">AI Data Centers : What to Know About Their Water and Energy Use</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-copyright-push-new-rules-australia-ip-solved-msm6c">AI , Copyright , and the Push for New Rules in Australia</a></li>
<li><a href="https://theprimary.com/ai-tech/2026-09-10/hinton-anthropic-ai-extinction-risk">Geoffrey Hinton backs Anthropic researcher on 10% extinction risk</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#data centres`, `#Australian politics`, `#public opinion`, `#technology regulation`

---

