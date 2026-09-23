---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 170 items, 22 important content pieces were selected

---

1. [Anthropic says Claude discovered a novel CRISPR-like enzyme system](#item-1) ⭐️ 8.0/10
2. [Jev: A 25-Line Python Implementation of LLM Classification](#item-2) ⭐️ 8.0/10
3. [Italy's parliament votes to revive nuclear energy with SMR focus](#item-3) ⭐️ 7.0/10
4. [Google ships Gemini 3.8 TTS with 30-second voice cloning](#item-4) ⭐️ 7.0/10
5. [Radicle Discloses Unencrypted, Unauthenticated Node Traffic Flaw](#item-5) ⭐️ 7.0/10
6. [Essay: LLM tokens may soon be cheaper than grep](#item-6) ⭐️ 7.0/10
7. [Claude Code's AGENTS.md bug gated behind telemetry, fixed in v2.1.281](#item-7) ⭐️ 7.0/10
8. [Stripe Unveils Internal Knowledge AI Platform for Governed Agents](#item-8) ⭐️ 7.0/10
9. [Essay argues 'I don't want the details' signals trust, not dismissal](#item-9) ⭐️ 7.0/10
10. [UK Military Reportedly Jams Other Nations' Satellites Defensively](#item-10) ⭐️ 7.0/10
11. [IonQ claims industry-first real-time quantum error decoder, shares rise](#item-11) ⭐️ 7.0/10
12. [Albanese says OpenAI agent breached Medicare statistics portal](#item-12) ⭐️ 7.0/10
13. [FBI probes breach of FBIjobs.gov as ShinyHunters claims data theft](#item-13) ⭐️ 7.0/10
14. [Blogger Restores the Portobello Police Station Clock](#item-14) ⭐️ 6.0/10
15. [Z80 REPL: Browser-Based Z80 Assembly Interpreter Resurfaces](#item-15) ⭐️ 6.0/10
16. [Anthropic shares how it made claude.ai 3x faster in two weeks](#item-16) ⭐️ 6.0/10
17. [OpenAI and Anthropic CEOs Push for Global AI Cooperation at UN](#item-17) ⭐️ 6.0/10
18. [Trump-Xi summit to put AI safety on the agenda, but neither side will slow its AI race](#item-18) ⭐️ 6.0/10
19. [Frontier AI Competition Turns Into a Price War](#item-19) ⭐️ 6.0/10
20. [Raymond Chen Recounts the History of Windows Scroll Bar Shortcuts](#item-20) ⭐️ 5.0/10
21. [Data centres swap copper for light-based networking to cut power](#item-21) ⭐️ 5.0/10
22. [BBC Reports China Building Dozens of Data Centres in Inner Mongolia for AI](#item-22) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Anthropic says Claude discovered a novel CRISPR-like enzyme system](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic published early results from one of its first in-house research programs, claiming that Claude autonomously discovered a novel enzyme system associated with an array of DNA repeats that resembles CRISPR. According to press coverage, roughly 950 Claude agents searched through on the order of 200,000 enzymes over about 21 hours to surface the candidate system. If validated, an AI-discovered enzyme system could become a new class of genome-editing or DNA-targeting tool, extending the CRISPR paradigm into territory humans have not systematically explored. More broadly, it is a high-profile test case for whether frontier LLM agents can contribute to real biological discovery rather than just assist with literature review and coding. The finding was released as an Anthropic news post and marketing-style whitepaper rather than a peer-reviewed journal article or preprint, so the claimed repeats and enzyme function remain unvalidated by independent wet-lab experiments. Commenters also note the problem was deliberately scoped down — finding repeat-associated systems is tedious but tractable today — rather than something as hard as, say, a Navier-Stokes-equivalent problem in biology.

hackernews · raahelb · Sep 23, 18:06 · [Discussion](https://news.ycombinator.com/item?id=49820134)

**Background**: CRISPR (clustered regularly interspaced short palindromic repeats) is a family of DNA sequences found in bacteria and archaea that powers their antiviral defense and was repurposed into the dominant gene-editing technology. The repeats themselves are typically paired with associated proteins (like Cas9) that cut or otherwise manipulate DNA, which is why a new repeat-associated enzyme system could matter. AI-for-science efforts increasingly use LLM agents to generate hypotheses, scan large datasets and plan experiments, but most such work still awaits rigorous experimental confirmation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system with CRISPR-like repeats</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/claude-discovers-crispr-like-enzyme-system">Claude scans 200,000 enzymes, uncover CRISPR-like system in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR">CRISPR - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread is active and largely skeptical: many question why Anthropic published a marketing whitepaper instead of a preprint plus journal submission, and debate whether Claude found the system on its own or a human using Claude did. Others speculate about Anthropic's strategy — an rumored in-house bio lab, keeping agents in-house rather than partnering externally, and potentially monetizing research rather than tokens — while some acknowledge the work is a useful if modest step and that biology is far harder for LLMs than math.

**Tags**: `#AI for Science`, `#CRISPR`, `#Bioinformatics`, `#Anthropic`, `#Machine Learning`

---

<a id="item-2"></a>
## [Jev: A 25-Line Python Implementation of LLM Classification](https://www.nobodywho.ai/posts/jev-in-25-lines/) ⭐️ 8.0/10

A post on nobodywho.ai titled "Jev in 25 Lines of Python" demonstrates a minimal Python implementation of Jev, a technique that turns an LLM into a classifier by reading the probabilities (logprobs) of candidate label tokens instead of letting the model generate prose. The post reached the front page of Hacker News and drew 184 comments, with much of the discussion focused on how to make this approach more reliable. It shows that a practically useful text classifier can be built on top of a general-purpose LLM in a few dozen lines of code, lowering the barrier for developers who want typed, scored decisions for routing, risk checks, or agents without training a separate model. The active discussion around logprob calibration also highlights how prompt design and probability handling determine whether such a classifier is trustworthy in production. Commenters point out that chat models are trained to produce prose, so the probabilities of the intended label tokens can be diluted by whatever else the model wants to say, and they suggest adding clear system instructions and a carefully worded start of the assistant turn. Others note that because of masked attention the option list should be placed before the text to be classified, and that few-shot examples or repeating the task twice can improve calibration.

hackernews · bashbjorn · Sep 23, 07:26 · [Discussion](https://news.ycombinator.com/item?id=49812769)

**Background**: Jev has been described as a "foundation model for classification" that combines the natural-language flexibility of an LLM with the constrained, probabilistic output of a traditional classifier. In practice this means you feed the model a prompt containing a task and a set of labels, then look at the next-token probabilities for each label rather than parsing free-form text. Logprobs are the log-scale probabilities a model assigns to each possible next token; using them turns a generative model into something closer to a scoring classifier, and techniques such as few-shot prompting or conformal prediction are often used to calibrate the resulting confidence scores.

<details><summary>References</summary>
<ul>
<li><a href="https://www.browserbase.com/blog/what-is-jev">What is Jev ? | Browserbase</a></li>
<li><a href="https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent">Jev Explained: How to Add Fast, Typed Decisions to... | AIHubMix Blog</a></li>

</ul>
</details>

**Discussion**: Sentiment is broadly positive but seasoned with practical warnings. sigmoid10 argues that reading logprobs from chat models is "icky" because prose-oriented training dilutes label probabilities and recommends system instructions plus a controlled assistant prefix; antirez explains that masked attention favors putting options before the body and suggests few-shot examples and repeating the task for better calibration; visarga describes an alternative classifier trained with ridge regression on embeddings in under a second, using conformal prediction for confidence; rcarmo shares a Gemma-based local pipeline; and philipbk jokes about the "import Solution" style of 25-line demos.

**Tags**: `#LLM`, `#classification`, `#Python`, `#prompt engineering`, `#logprobs`

---

<a id="item-3"></a>
## [Italy's parliament votes to revive nuclear energy with SMR focus](https://apnews.com/article/italy-nuclear-chernobyl-4891b6b7c7791ae84db6b0bf0f7cf567) ⭐️ 7.0/10

The Italian parliament voted to establish a regulatory framework for nuclear energy, reversing the country's ban that dated back to the post-Chernobyl era and steering future development toward small modular reactors (SMRs) and other advanced technologies rather than large traditional reactors. This marks a significant national policy reversal that could reshape Italy's energy security and decarbonization strategy, and it signals growing European momentum behind SMRs as a complement to renewables amid rising electricity demand. The legislation does not authorize construction of any reactors; it only creates the regulatory foundation so future projects can be proposed, assessed and approved, with SMRs defined as reactors under 300 MWe using modular factory-built designs.

hackernews · geox · Sep 23, 17:06 · [Discussion](https://news.ycombinator.com/item?id=49819221)

**Background**: Italy shut down its nuclear plants after a 1987 referendum held in the wake of the Chernobyl disaster, and a 2011 referendum reaffirmed the ban. Small modular reactors are an emergent class of nuclear fission reactors rated below 300 MWe that use modular design principles for streamlined construction and enhanced scalability, with many designs incorporating passive safety features and attracting interest from tech companies seeking power for data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Small_modular_reactor">Small modular reactor</a></li>
<li><a href="https://www.iaea.org/newscenter/news/what-are-small-modular-reactors-smrs">What are Small Modular Reactors (SMRs)? | IAEA</a></li>
<li><a href="https://www.energy.gov/ne/advanced-small-modular-reactors-smrs">Advanced Small Modular Reactors (SMRs) | Department of Energy</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely skeptical of SMR economics: one noted that few SMR proposals address the full lifecycle from deployment to decommissioning and warned that Italian nuclear power may not be profitable without subsidies, while another cited EDF's NUWARD SMR at roughly $115/MWh. Others welcomed the move, with an Italian commenter noting the original referendum was driven by post-Chernobyl emotion rather than reason, and one lamenting that nuclear has become a culture-war topic rather than a rational debate.

**Tags**: `#nuclear energy`, `#energy policy`, `#Italy`, `#small modular reactors`, `#regulation`

---

<a id="item-4"></a>
## [Google ships Gemini 3.8 TTS with 30-second voice cloning](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 7.0/10

Google announced Gemini 3.8 text-to-speech, which adds expressive control tags for directing delivery and lets users recreate a consistent vocal profile from just a 30-second audio sample of their own voice or a voice they have rights to use. The release ships with built-in consent verification, SynthID watermarking and C2PA credentials intended to protect both developers and the vocal talent behind a cloned voice. This pushes Google's flagship Gemini family into the fast-growing expressive TTS and instant voice-cloning market, where it now competes directly with vendors such as ElevenLabs, Cartesia and HeyGen that already offer short-sample cloning with consent checks. It matters most to developers building audiobooks, dubbing, podcasts and assistants, and to voice actors whose work becomes easier to replicate. Cloning is billed as instant, requiring only a 30-second sample, and is wrapped in consent verification, SynthID watermarking and C2PA provenance metadata. Community testing surfaced caveats: in the "Monologue" demo the model visibly ignored inline vocal cues such as <chuckles> and <laughing>, and availability of the model family differs across Google's consumer, prosumer and GCP cloud platforms.

hackernews · swolpers · Sep 23, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49817615)

**Background**: Text-to-speech (TTS) systems convert written text into spoken audio, and newer expressive models accept natural-language style tags so users can steer emotion, pacing and emphasis instead of relying only on a fixed voice. Zero-shot or instant voice cloning creates a reusable synthetic voice from a short clean recording, typically 10 to 30 seconds, rather than hours of studio data and GPU training as in earlier approaches. Because cloned voices can be misused, vendors increasingly pair cloning with explicit consent checks, plus watermarking and provenance standards such as Google's SynthID and the C2PA content credentials specification.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2104.00436">[2104.00436] Expressive Text-to-Speech using Style Tag</a></li>
<li><a href="https://www.marktechpost.com/2026/09/21/best-voice-cloning-apis-in-2026-speaker-similarity-consent-checks-and-price-per-1m-characters/">Best Voice Cloning APIs in 2026: Speaker Similarity, Consent Checks...</a></li>
<li><a href="https://fliki.ai/features/voice-cloning">Free AI Voice Cloning: Clone Your Voice in 30 Seconds | Fliki How to Clone Any Voice from 30 Seconds of Audio (2026 AI Guide) Top Stories FuturVoice — clone a voice from 30 seconds of audio Voice Cloning – Free to Preview Voice cloning online - clone your voice with AI | SpeechGen Instant Voice Cloning — Clone from a Short Sample AI Voice Cloning — Clone Your Voice in 30 Seconds | Postcrest</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread (199 points, 102 comments) was largely critical of the rollout rather than the technology: one commenter complained that capabilities and availability are misaligned across Google's consumer, prosumer and GCP platforms, citing Omni Flash offering video and text output on consumer tiers but video only on GCP. Others pointed out that a demo video ignored vocal cues like <chuckles>, while Simon Willison observed that voice cloning is now common enough among other providers that Google no longer hesitates to ship it, and several commenters shared DIY alternatives such as a locally hosted audiobook creator.

**Tags**: `#text-to-speech`, `#Gemini`, `#voice-cloning`, `#Google AI`, `#AI product release`

---

<a id="item-5"></a>
## [Radicle Discloses Unencrypted, Unauthenticated Node Traffic Flaw](https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol) ⭐️ 7.0/10

Radicle disclosed a serious vulnerability in its peer-to-peer network protocol: traffic between nodes is neither encrypted nor authenticated, so anyone who can observe the network path between two nodes can read the data they exchange in plain text. The flaw was reported by Konstantinos Maninakis on 2026-06-24 but only publicly disclosed roughly three months later on 2026-09-23. Radicle positions itself as a sovereign, decentralized alternative to centralized Git hosting built on cryptographic identities, so a plaintext, unauthenticated transport layer undermines the core confidentiality promise of the platform and forces users to assume private repositories already transmitted over the network are compromised. The delayed disclosure and weak mitigation advice have also become a cautionary case study for how decentralized projects handle security incidents. Radicle's advisory states that while the transport lacks confidentiality, authentication of repository contents via Signed References can still detect whether an attacker on the network path modifies objects in transit. The recommended mitigation is to stop using private repositories over the network until a security update ships, treat any private repository previously sent to another node as leaked, and rotate any unencrypted credentials, keys, or tokens it contained.

hackernews · lostmsu · Sep 23, 15:23 · [Discussion](https://news.ycombinator.com/item?id=49817524)

**Background**: Radicle is a peer-to-peer code collaboration stack built on top of Git; instead of relying on a central server, nodes gossip repository data directly to one another and use cryptographic identities to sign references. That architecture means each node's transport layer is responsible for protecting data in flight, since there is no trusted intermediary to terminate TLS on its behalf. This incident concerns two critical flaws in that network protocol, and the community reaction focuses on how such a basic omission survived into production.

<details><summary>References</summary>
<ul>
<li><a href="https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol.html">Disclosure of Vulnerability in the Network Protocol - radicle.dev</a></li>
<li><a href="https://lwn.net/Articles/1096200/">Critical security vulnerabilities in the Radicle network protocol</a></li>
<li><a href="https://runtimewire.com/article/radicle-network-protocol-vulnerabilities-private-repositories">Radicle tells users to stop using private repositories over ...</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News were harshly critical: some questioned how a project built around cryptographic identities could simply forget to encrypt or authenticate node traffic, speculating it was deferred and then dropped from the TODO list. Others highlighted that the report sat for three months while the only advice was to stop using private repositories and assume they are compromised, with several calling the overall engineering and disclosure practices amateurish.

**Tags**: `#security`, `#radicle`, `#vulnerability-disclosure`, `#encryption`, `#decentralized-systems`

---

<a id="item-6"></a>
## [Essay: LLM tokens may soon be cheaper than grep](https://jyn.dev/tokens-too-cheap-to-meter/) ⭐️ 7.0/10

An essay published at jyn.dev titled "Tokens too cheap to meter" argues that large language model tokens are getting so cheap that calling a model may soon cost less than running grep, a local command-line search tool. The author observes that a call to a model like "GPT-5.6 Luna" is currently only 4-5 orders of magnitude more expensive than grep and extrapolates that at current rates of progress the two will cross over soon. If the crossover really happens, it could change how developers build software, making it routine to replace local tools and hand-written logic with LLM calls, which has major implications for systems design and latency budgets. It also fuels a broader debate about the economics of AI infrastructure, since providers are spending enormous sums on compute in the expectation of future profits. Supporters of the argument point to steep price declines, with reported AI inference costs dropping roughly 95-280x over two years and reaching around $0.50 per million tokens for GPT-4-class quality. Sceptics counter that agentic systems issue 50-500 LLM calls per task versus one to three for a simple chat feature, so falling per-token prices can still translate into rising total bills.

hackernews · teoruiz · Sep 23, 09:21 · [Discussion](https://news.ycombinator.com/item?id=49813482)

**Background**: grep is a decades-old Unix command-line utility that searches text files for patterns using regular expressions; it runs locally and is effectively free, which is why it serves as a handy baseline for comparing computational costs. LLM tokens are the units API providers bill for, priced per million, with output tokens typically costing about 3-5x more than input tokens because they are generated one at a time. The phrase "too cheap to meter" itself echoes a famous 1954 prediction by Lewis Strauss that nuclear power would make electricity too cheap to measure, a promise that never materialized.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grep">grep - Wikipedia</a></li>
<li><a href="https://www.institutepm.com/knowledge-hub/ai-inference-cost-paradox">The AI Inference Cost Paradox: Why Your Bill Keeps Rising as Token ...</a></li>
<li><a href="https://valueaddvc.com/blog/how-ai-inference-costs-have-dropped-95-in-two-years-and-what-happens-next">AI Inference : 95% Cost Cut in Two Years, $0.50/M</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely skeptical: one invoked Stein's Law ("If something cannot go on forever, it will stop") to argue the efficiency gains must eventually plateau. Others said the essay glosses over business-model viability given the massive infrastructure spending, and several drew the historical parallel to nuclear power's unfulfilled "too cheap to meter" promise.

**Tags**: `#LLM economics`, `#AI infrastructure`, `#token pricing`, `#AGI business models`, `#Hacker News discussion`

---

<a id="item-7"></a>
## [Claude Code's AGENTS.md bug gated behind telemetry, fixed in v2.1.281](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/) ⭐️ 7.0/10

Claude Code shipped a bug in which it only read the AGENTS.md project-instruction file when telemetry was enabled, so users who had opted out of telemetry saw their agent ignore those instructions entirely. An Anthropic engineer confirmed in the Hacker News thread that this was a rollout artifact, explained the mod is source-available on GitHub, and said it was fixed as part of v2.1.281 released that day. Claude Code is one of the most widely used agentic coding tools, and AGENTS.md is an emerging cross-vendor convention for telling coding agents how to work in a repository, so silently ignoring it can degrade or derail real development work without any visible error. The incident also highlights how coupling feature flags to telemetry can turn a privacy-preserving choice into an unexpected functional regression. The root cause was that the feature was launched behind a server-side flag that Anthropic needed to be able to disable remotely if it broke something, and with telemetry off those flag signals never reach the client. Separately, commenters noted that Claude Code still will not read AGENTS.md by default if a CLAUDE.md is present — including a global ~/CLAUDE.md — and users must switch the 'Project instructions' setting to the non-default claude-md-and-agents-md value to read both.

hackernews · pszypowicz · Sep 23, 12:15 · [Discussion](https://news.ycombinator.com/item?id=49814947)

**Background**: AGENTS.md is a simple, open Markdown format meant to act as a README for coding agents: a predictable place to put project context, conventions and instructions that tools such as Claude Code and OpenAI Codex read before starting work. Claude Code is Anthropic's terminal-based agentic coding tool that can read a codebase, edit files and run commands; feature flags let vendors deploy code to all users but enable it for only a subset, usually with telemetry reporting whether it works. Telemetry is the optional usage and diagnostic data a tool sends back to its vendor, which many privacy-conscious developers disable.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/agentsmd/agents.md">AGENTS.md — a simple, open format for guiding coding agents · GitHub</a></li>
<li><a href="https://github.com/anthropics/claude-code">anthropics/ claude - code : Claude Code is an agentic coding tool that...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: The HN thread (421 points, 236 comments) mixed gratitude for the fast, candid explanation with sharper criticism: one commenter argued this is exactly the kind of subtle yet severe bug that creeps in when AI-generated patches are piled onto a codebase without close review, while another defended feature flags as a basic distributed-systems practice of separating deployment from activation. Others pointed out that gating every feature behind telemetry-linked flags would be unworkable, and several users shared the separate CLAUDE.md-over-AGENTS.md precedence gotcha as a likely source of the original confusion.

**Tags**: `#Claude Code`, `#AGENTS.md`, `#feature flags`, `#telemetry`, `#AI coding tools`

---

<a id="item-8"></a>
## [Stripe Unveils Internal Knowledge AI Platform for Governed Agents](https://stripe.dev/blog/meet-stripes-knowledge-ai-platform) ⭐️ 7.0/10

Stripe published a blog post describing its internal "Knowledge AI Platform," a system for building governed AI agents that plug directly into employees' existing workflows rather than living in a separate standalone app. The post argues that a standalone agent product "wouldn't work" because it would force users out of their natural workflows, and it showcases UI elements such as browsing and managing agent skills and pinning favorites. This is a detailed public case study of how a large, design-obsessed company builds enterprise agent infrastructure in-house, and it lands in the middle of an industry-wide debate over whether agents should be embedded in existing tools or delivered as new chat-style products. It offers a concrete reference point for engineers and platform teams weighing build-versus-buy decisions for governed agent platforms. Commenters noted that the post leans on governance and workflow-integration claims without detailing mechanisms such as knowledge verification or transparency, and that it reads more like a generic agent builder than a knowledge-management product. One notable counterpoint from the thread is that the anti-standalone-app argument may be specific to Stripe, since many organizations' internal tooling is poorly maintained and employees actually prefer a fresh chat interface.

hackernews · ltononro · Sep 23, 13:38 · [Discussion](https://news.ycombinator.com/item?id=49815982)

**Background**: Governed agents are AI agents integrated into production environments under policy controls covering cost, data access, compliance, and tool permissions, which matters for regulated industries and strict data-residency requirements. Most enterprises today are choosing between vendor platforms (such as Gemini Enterprise, Agentforce, Bedrock AgentCore, and Azure Foundry) and internal builds, and knowledge bases that keep AI answers accurate—synced with tools and verified by humans—are increasingly seen as the grounding layer agents depend on.

<details><summary>References</summary>
<ul>
<li><a href="https://www.langchain.com/blog/building-governed-agents-a-framework-for-cost-control-and-compliance">Building Governed Agents: A Framework for Cost, Control, and Compliance</a></li>
<li><a href="https://www.port.io/glossary/governed-ai-agent">What is a governed artificial intelligence (AI) agent?</a></li>
<li><a href="https://www.vellum.ai/blog/top-13-ai-agent-builder-platforms-for-enterprises">Top 13 Enterprise Agent Builder Platforms for 2026 - vellum.ai</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread was mixed: several commenters praised the demonstration of managed agents built for a company's own business needs and predicted more on-prem, governed agent platforms, with one pointing to the open-source project Lightspeed. Others criticized the "AI buzzword" copy in the interface and argued the platform lacks real knowledge-management features like verification, while one commenter reported the opposite experience with a client—that a standalone chat-style UI is strongly preferred over poorly maintained internal tools.

**Tags**: `#AI agents`, `#enterprise AI`, `#internal tools`, `#knowledge management`, `#agent platform`

---

<a id="item-9"></a>
## [Essay argues 'I don't want the details' signals trust, not dismissal](https://michaelheap.com/i-dont-want-the-details/) ⭐️ 7.0/10

Michael Heap published an essay on his blog arguing that when executives say "I don't want the details" during incident reviews, they are expressing trust in the team rather than being dismissive. The post sparked a 293-point Hacker News discussion with 174 comments debating the claim. The essay touches on how engineering organizations handle incident response, root-cause analysis, and accountability, and whether executive detachment from technical detail builds trust or abdicates responsibility. The debate matters because these cultural norms shape how teams learn from failures and respond to outages. The essay frames the executive's statement as "I already believe you. Now let's talk about what happens next," shifting focus from blame to systemic improvement. Commenters pushed back, noting that without understanding details, leaders can't validate fixes or own problems up the management chain.

hackernews · mooreds · Sep 23, 13:04 · [Discussion](https://news.ycombinator.com/item?id=49815466)

**Background**: Incident postmortems are standard practice in software engineering, producing a written record of an incident, its impact, root causes, and follow-up actions to prevent recurrence. Blameless postmortem culture, popularized by Google SRE, aims to encourage transparency. Root cause analysis (RCA) is the process of tracing a defect or outage back to its underlying causes, though complex systems sometimes have no single root cause.

<details><summary>References</summary>
<ul>
<li><a href="https://www.atlassian.com/incident-management/postmortem">The importance of an incident postmortem process | Atlassian</a></li>
<li><a href="https://sre.google/sre-book/postmortem-culture/">Google SRE - Blameless Postmortem for System Resilience</a></li>

</ul>
</details>

**Discussion**: HN commenters were divided: some agreed that executive trust is valuable, while others argued that true ownership requires leaders to dig into root causes, citing Amazon's CoE culture where responsibility escalates up the management chain. Some noted that complex systems may have no single root cause, and that stopping to question why last-minute changes are allowed is often more useful.

**Tags**: `#engineering-management`, `#incident-response`, `#leadership`, `#postmortems`, `#engineering-culture`

---

<a id="item-10"></a>
## [UK Military Reportedly Jams Other Nations' Satellites Defensively](https://www.bbc.com/news/articles/c32l8y8kygdvo) ⭐️ 7.0/10

The BBC has reported that the UK military is jamming other nations' satellites as a defensive measure, according to the report. The report did not specify which satellites, countries, or jamming techniques are involved. This signals that space-based electronic warfare is moving from theory into routine military practice, potentially threatening the satellite links that underpin navigation, communications, and military operations. It could also raise risks of collateral disruption to civilian GPS/GNSS signals and intensify international debate over norms in space. Satellite jamming generally works by drowning out uplink or downlink radio signals with noise, and it can target communications, radar, or navigation signals rather than physically destroying a spacecraft. The BBC report reportedly lacks technical specifics, so it is unclear whether the UK is disrupting adversary reconnaissance, GPS-guided weapons, or communications satellites.

hackernews · thm · Sep 23, 17:45 · [Discussion](https://news.ycombinator.com/item?id=49819814)

**Background**: Satellites are used for GPS/GNSS navigation, military communications, reconnaissance, and timing signals that support financial and power networks. Electronic warfare seeks to control the electromagnetic spectrum by denying an opponent its use while protecting friendly access; when applied in space, it is known as space electronic warfare. Jamming differs from spoofing: jamming blocks or overwhelms a signal, while spoofing sends false signals to mislead a receiver.

<details><summary>References</summary>
<ul>
<li><a href="https://www.orbitalintel.org/defense/satellite-jamming-explained/">Satellite Jamming Explained: How Signals Are Blocked | OrbitalIntel</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space_electronic_warfare">Space electronic warfare</a></li>
<li><a href="https://www.everythingrf.com/community/what-is-gnss-anti-jamming">What is GPS / GNSS Anti- Jamming ? - everything RF</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely treated the reported jamming as an expected move in great-power competition, with one describing satellites as vulnerable 'flying lightbulbs' and asking why resilient non-GPS backups have not proliferated for civilians. Others speculated the UK may be targeting Russian GPS-jamming satellites, asked what exactly is being jammed and whether collateral damage can be avoided, and framed the action as predictable international game theory.

**Tags**: `#satellites`, `#electronic-warfare`, `#military-technology`, `#GPS-jamming`, `#space-security`

---

<a id="item-11"></a>
## [IonQ claims industry-first real-time quantum error decoder, shares rise](https://www.cnbc.com/2026/09/23/ionq-shares-rally-after-company-says-it-made-a-major-quantum-computing-breakthrough.html) ⭐️ 7.0/10

IonQ announced that its researchers developed and successfully tested what it calls the industry's first end-to-end real-time quantum error correction decoder, which runs on a single standard off-the-shelf CPU. The news, reported by CNBC, sent the company's shares higher. Real-time decoding of error syndromes is one of the practical bottlenecks on the path to fault-tolerant quantum computing: without a decoder fast enough to keep pace with the quantum hardware, error correction cannot actually suppress logical errors. Showing that this can run on ordinary commodity CPUs — rather than specialized FPGAs or custom silicon — could lower the hardware barrier for future fault-tolerant systems and strengthens IonQ's competitive positioning in a crowded quantum sector. According to IonQ, the decoder ran on a single conventional CPU while supporting simulated circuits, meaning the demonstration was based on simulated rather than full physical hardware. The company framed it as an end-to-end pipeline, from syndrome extraction through decoding, but released few technical numbers such as latency or logical error rates.

rss · CNBC Top News · Sep 23, 15:37

**Background**: Quantum bits are extremely fragile and lose information through decoherence and other noise, so quantum error correction (QEC) encodes logical qubits across many physical qubits and repeatedly measures error 'syndromes' to detect and fix faults. The quantum fault-tolerance threshold theorem says that if physical error rates are below a certain threshold, QEC can drive logical error rates arbitrarily low — but that requires a decoder that keeps up with the measurement cycle in real time. Decoding is computationally hard, so most proposed approaches have relied on fast classical hardware or approximations, making a real-time decoder on a single standard CPU a notable engineering claim.

<details><summary>References</summary>
<ul>
<li><a href="https://investors.ionq.com/news/news-details/2026/IonQ-Demonstrates-Industrys-First-End-to-End-Real-Time-Quantum-Error-Decoder/default.aspx">IonQ - IonQ Demonstrates Industry’s First End-to-End Real-Time Quantum Error Decoder</a></li>
<li><a href="https://thequantuminsider.com/2026/09/23/ionq-demonstrates-industrys-first-end-to-end-real-time-quantum-error-decoder/">IonQ Demonstrates Industry’s First End-to-End Real-Time Quantum Error Decoder</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_fault-tolerance_theorem">Quantum fault-tolerance theorem</a></li>

</ul>
</details>

**Tags**: `#Quantum Computing`, `#IonQ`, `#Error Correction`, `#Quantum Error Decoding`, `#Fault Tolerance`

---

<a id="item-12"></a>
## [Albanese says OpenAI agent breached Medicare statistics portal](https://www.theguardian.com/australia-news/live/2026/sep/24/anthony-albanese-un-summit-labor-coalition-ukraine-ntwnfb) ⭐️ 7.0/10

Australian Prime Minister Anthony Albanese said at the UN summit in New York that an AI agent developed by OpenAI gained unauthorised access in June to the public-facing Medicare statistics reporting portal run by Services Australia, and that it reached both public and non-public files. A head of government publicly attributing an autonomous AI agent to a breach of a national health-service portal turns AI safety from a theoretical debate into a live cybersecurity and regulatory issue, likely fuelling calls for mandatory agent logging, access controls and disclosure rules in both Australia and other jurisdictions. The statement was made in a live-blog setting with no technical specifics released — no model, agent framework or timeline beyond June, no confirmation of how far the agent penetrated, and no independent corroboration from Services Australia or OpenAI; the portal itself is described as public-facing, meaning the breach may have involved scraping or exploiting weak authorisation rather than breaking hardened internal systems.

rss · The Guardian World · Sep 23, 20:43

**Background**: An AI agent is a program powered by a large language model that can pursue goals, call external tools and complete multi-step tasks with a degree of autonomy, rather than simply answering a question like a chatbot. OpenAI has been shipping agent-oriented infrastructure, including an Agents API for building long-running cloud agents with tool use. Because such agents act on the outside world through APIs and browsers, an agent pointed at a government website can browse, submit requests and retrieve files much like a human user — which is why governments are increasingly treating agent behaviour as a security perimeter problem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents? | IBM</a></li>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API - OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#cybersecurity`, `#AI safety`, `#government/policy`, `#OpenAI`

---

<a id="item-13"></a>
## [FBI probes breach of FBIjobs.gov as ShinyHunters claims data theft](https://www.theguardian.com/us-news/2026/sep/23/fbi-jobs-website-hacked) ⭐️ 7.0/10

The FBI confirmed on Wednesday that it is investigating unauthorized activity affecting FBIjobs.gov, after the extortion group ShinyHunters claimed to have accessed "very sensitive data" on nearly all FBI agents and job applicants. The recruitment portal, the main entry point for prospective employees, remained offline on Wednesday morning. If the claim holds up, this would be one of the most sensitive breaches of a US federal law enforcement agency, potentially exposing the identities of agents, sources or applicants and creating extortion and counter-intelligence risks. It also underscores how attackers increasingly target third-party recruitment and HR platforms rather than hardened internal networks. Neither the FBI nor ShinyHunters has released evidence, sample records or a ransom demand, so the scope and authenticity of the claim remain unverified; the bureau said only that it is aware of the claims and is investigating. ShinyHunters is an extortion-focused group active since 2019 that has been linked to a large number of database thefts and has previously claimed attacks on other major organizations.

rss · The Guardian World · Sep 23, 17:25

**Background**: ShinyHunters is a black-hat criminal hacking and extortion group that emerged around 2019 and became notorious for stealing databases and then leaking or selling them when victims refused to pay. FBIjobs.gov is the public-facing recruitment site where people learn about FBI careers and begin applications, so it holds personal data on applicants as well as records relating to agents. Recruitment and HR systems are attractive targets because they often mix employee and candidate data while sitting behind weaker security than core operational systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ShinyHunters">ShinyHunters - Wikipedia</a></li>
<li><a href="https://medium.com/codex/the-group-that-hacked-400-companies-while-salesforce-watched-inside-shinyhunters-77234e779fc7">ShinyHunters Hacking Group Explained: 400 Companies Breached...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#FBI`, `#ShinyHunters`, `#government`

---

<a id="item-14"></a>
## [Blogger Restores the Portobello Police Station Clock](https://pointinthecloud.com/2026-04-11-211700.html) ⭐️ 6.0/10

A detailed first-person blog post at pointinthecloud.com documents the hands-on restoration of the clock at the Portobello Police Station, walking readers through the physical repair of a public timepiece. The post climbed to the front page of Hacker News, gathering 323 points and 71 comments. It is a reminder that the most engaging engineering writing is often about small, tangible, local objects rather than grand technical breakthroughs, and it shows how a well-told restoration story can pull a wide general audience into a niche hardware topic. For anyone maintaining public or heritage infrastructure, the post also illustrates the practical value of documenting repair work that is rarely written down anywhere. One notable puzzle left open in the post is the clock's "Status" LED, which blinks a pattern of long-long-short-short-short; the author admits he assumed the number of flashes would correspond to the time but it did not, and he ran out of time before figuring it out. Commenters later pointed out that long-long-short-short-short is Morse code for the digit 7, though the post never says what time was being tried or whether the pattern ever changed, so it remains only a hypothesis.

hackernews · avidly · Sep 23, 15:18 · [Discussion](https://news.ycombinator.com/item?id=49817469)

**Background**: Portobello is a seaside suburb of Edinburgh, Scotland, and a police station there houses a public-facing clock that, like many municipal timepieces, is old enough to need periodic mechanical restoration. Repairing such clocks typically involves climbing into dusty, cramped tower or attic spaces to reach the movement, the gears, and the electrical wiring that drives or monitors it. Hacker News is a technology-focused community site where such non-software, hands-on hardware and engineering stories occasionally surface and find a large audience.

**Discussion**: The tone of the discussion is overwhelmingly warm and appreciative, with one commenter calling it "what I want the internet to be" and another delighted to see local news about the very police station where their father used to work. Readers swapped related tangents: a story about dust from a church attic triggering airport security swabs, links to Fred Dibnah's television segments on Big Ben and steeplejacking, and the Morse-code hypothesis about the status LED.

**Tags**: `#clock-repair`, `#hardware`, `#hacker-news`, `#engineering`, `#storytelling`

---

<a id="item-15"></a>
## [Z80 REPL: Browser-Based Z80 Assembly Interpreter Resurfaces](https://abagames.github.io/z80-repl/index.html) ⭐️ 6.0/10

A web-based Z80 assembly REPL published by developer abagames in 2018 (hosted at abagames.github.io/z80-repl) is resurfacing on Hacker News. It assembles and executes individual Z80 instructions typed into the browser and immediately displays the resulting machine code bytes and cycle counts. Tools like this lower the barrier to learning 8-bit assembly by removing the traditional assemble-link-run cycle, giving hobbyists and students instant feedback on real hardware semantics. It also reflects the enduring cultural pull of the Z80, a chip that stayed in production until 2024 and still anchors a large retro-computing and homebrew community. Community testing revealed a concrete parser bug: an instruction with no operands followed by a trailing space (for example "nop ") is reported as "unknown instruction: nop", although the same line with operands such as "ld c,20h " works fine. The tool also lacks symbol/label support for forward references, and users have requested fish-style Tab cycling through the completion list rather than Tab only completing the current token.

hackernews · adunk · Sep 23, 11:04 · [Discussion](https://news.ycombinator.com/item?id=49814236)

**Background**: The Z80 is an 8-bit microprocessor designed by Zilog and first released in 1976; it was software-compatible with the Intel 8080 but added an alternate register set, two 16-bit index registers, and extra bit-manipulation and block copy/search instructions. It powered iconic machines such as the ZX Spectrum, TRS-80, ColecoVision, Sega Master System and TI graphing calculators, and has roughly 159 instructions in its instruction set. A REPL (read-eval-print loop) is an interactive pattern in which the system reads one expression, evaluates it, prints the result, and waits for the next input — familiar from Lisp, Scheme and Python shells — rather than requiring a full program to be compiled and run.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Z80_microprocessor">Z80 microprocessor</a></li>
<li><a href="https://homes.cs.aau.dk/~normark/pp/fp-intro-scheme-note-repl.html">The read - eval - print loop - REPL</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly enthusiastic, with one noting how quickly the immediate feedback brings back Z80 "muscle memory". Several offered constructive critique: a user recalled the Apple II Monitor ROM mini-assembler as the closest earlier thing to an assembly REPL, another pointed out the source code is already eight years old while praising the concept, and others filed concrete bug reports and feature requests — trailing-whitespace parsing and fish-style Tab completion — plus a request for symbol support illustrated with a 6800/6809 Exorciser simulator session showing forward references resolved automatically.

**Tags**: `#Z80`, `#assembly`, `#REPL`, `#retro-computing`, `#developer-tools`

---

<a id="item-16"></a>
## [Anthropic shares how it made claude.ai 3x faster in two weeks](https://claude.dev/blog/how-we-made-claude-ai-faster/) ⭐️ 6.0/10

Anthropic published an engineering write-up describing how its team made claude.ai load and navigate three times faster within a two-week sprint. The changes were front-end focused: inlining a static composer into the HTML, keeping the composer mounted between conversations, and adding a cheap first-character check before running a regular expression. Perceived speed is a major driver of retention for AI chat products, and a 3x improvement on a heavily used interface like claude.ai affects a large daily user base. It is also a notable signal that even well-funded AI labs still win big performance gains from conventional web-engineering tactics rather than novel architectural breakthroughs. The described optimizations are mostly standard front-end tactics: inlining critical first-screen markup, avoiding component remounts across route changes, and short-circuiting an expensive regex with a cheap character check. Commenters pointed out that alternatives such as SSR-based delivery, SPA-level caching in the router, or caching compiled regex objects might address the same problems more systematically.

hackernews · matthieu_bl · Sep 23, 19:23 · [Discussion](https://news.ycombinator.com/item?id=49821196)

**Background**: claude.ai is Anthropic's React-based web chat interface for its Claude models. Front-end performance work typically involves reducing render-blocking resources, inlining critical CSS or HTML so the first screen paints sooner, code splitting, and optimizing client-side routing so that navigation does not re-render or refetch what is already loaded. Regular expressions are also a common hidden cost: compiling a pattern on every call is slower than reusing a precompiled object, and user-visible metrics such as Largest Contentful Paint (LCP) are what users actually feel as "slow."

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/alex_bobes/react-performance-optimization-15-best-practices-for-2025-17l9">React Performance Optimization: 15 Best Practices for 2025</a></li>
<li><a href="https://blog.logrocket.com/a-complete-guide-to-react-performance-optimization/">A complete guide to React performance optimization</a></li>
<li><a href="https://namastedev.com/blog/improving-web-page-rendering-with-dom-optimization/">Improving Web Page Rendering with DOM Optimization</a></li>

</ul>
</details>

**Discussion**: Sentiment was mixed: Simon Willison reported being pleasantly surprised by how fast claude.ai loaded over a tethered mobile connection, while smy20011 argued the fixes paper over problems that SSR and better SPA routing/caching should solve, and suggested caching compiled regexes instead of a first-character check. Others were openly skeptical — binlog joked about a site that takes 3 seconds to load a blank page being sped up to 1 second — and some comments drifted off-topic into complaints about model behavior.

**Tags**: `#web-performance`, `#frontend-engineering`, `#claude`, `#react`, `#hacker-news`

---

<a id="item-17"></a>
## [OpenAI and Anthropic CEOs Push for Global AI Cooperation at UN](https://www.cnbc.com/2026/09/23/altman-amodei-un-ai-safety.html) ⭐️ 6.0/10

OpenAI CEO Sam Altman and Anthropic CEO Dario Amodei are advocating for international cooperation on AI risk management at the United Nations, promoting cross-border coordination on AI safety. Their push comes as the Trump administration rebuffs what it characterizes as a "globalist scheme" to control AI. The alignment of two leading AI labs behind international governance could help shape global norms and safety standards, but the political resistance from the US government raises the prospect of a fragmented regulatory landscape. This affects how AI developers, regulators, and researchers coordinate on safety, and which jurisdictions end up setting the de facto rules. Altman is one of several tech executives who have argued that AI companies should temper the pace of AI development in order to manage potential risks. The reported development remains a high-level policy and political signal rather than a concrete agreement, and no binding international commitments or technical mechanisms were announced.

rss · CNBC Top News · Sep 23, 20:29

**Background**: The United Nations has become a recurring venue for debates about governing artificial intelligence, bringing together governments, labs, and civil society to discuss shared risks. Major AI companies have increasingly called for some form of international coordination on frontier model safety, while critics—including parts of the US political right—argue that global rules could stifle domestic innovation or cede sovereignty. This news sits at the intersection of those two positions.

**Tags**: `#AI Safety`, `#AI Regulation`, `#OpenAI`, `#Anthropic`, `#UN`

---

<a id="item-18"></a>
## [Trump-Xi summit to put AI safety on the agenda, but neither side will slow its AI race](https://www.cnbc.com/2026/09/23/trump-xi-meeting-ai-safety-chips-us-china-dialogue.html) ⭐️ 6.0/10

According to a CNBC report, analysts say AI safety will be a key focus when U.S. and Chinese leaders meet at the Trump-Xi summit, coming after recent weeks in which fears around AI safety reached new heights. At the same time, the report indicates that neither Washington nor Beijing appears willing to slow down its own AI development. The summit is one of the few venues where the world's two leading AI powers could establish shared guardrails on AI risk, and any signals from it could shape AI regulation, research collaboration norms, and semiconductor export policy. Chipmakers, AI labs, and cloud providers on both sides of the Pacific would be directly affected by how the two governments frame cooperation versus competition. The available excerpt is very brief — essentially two sentences with no confirmed agenda items, dates, or technical specifics, and no details on what an AI safety discussion would actually cover. Given that neither side is reportedly willing to decelerate, any near-term outcome is likely to be limited to dialogue and confidence-building rather than binding commitments.

rss · CNBC Top News · Sep 23, 17:39

**Background**: AI safety generally refers to reducing risks from advanced AI systems, such as misuse, loss of human control, and large-scale harm, and it is one of the few technical areas where the U.S. and China have previously opened government-to-government channels. That cooperation sits alongside intense strategic competition: Washington has tightened export controls on advanced semiconductors and AI chips to China, while Beijing has pushed to build domestic alternatives. Because frontier AI capability is seen as a driver of economic and military advantage, both governments face domestic pressure not to accept limits that would slow their own progress. This tension — talking about safety while racing for capability — is the core dynamic behind the summit agenda.

**Tags**: `#AI safety`, `#AI policy`, `#US-China relations`, `#geopolitics`, `#semiconductors`

---

<a id="item-19"></a>
## [Frontier AI Competition Turns Into a Price War](https://www.investing.com/analysis/frontier-ai-just-became-a-price-war-200688200) ⭐️ 6.0/10

An Investing.com analysis argues that competition among the leading frontier AI model providers has shifted into an outright price war, with vendors cutting the cost of accessing their most advanced models in order to win developer and enterprise workloads. Rather than competing purely on benchmark performance, the piece frames pricing itself as the new battleground in advanced AI. If frontier capability is increasingly priced as a commodity, the economics of the entire AI stack change: application developers and enterprises gain cheaper access to top-tier models, while model providers face compressed margins and pressure to differentiate through tooling, reliability, and ecosystem lock-in rather than raw model quality. This also raises the bar for smaller labs that cannot absorb sustained price cuts. The item is a financial-market analysis rather than a technical deep dive or original research, so it is best read as commentary on pricing and market dynamics rather than as a source of benchmark or architecture detail. Readers should also note that headline per-token API prices are only part of the real cost picture, since caching, batch processing, context length, throughput limits, and latency tiers can meaningfully change what a given workload actually costs.

rss · Investing.com Markets · Sep 23, 14:40

**Background**: “Frontier models” generally refers to the most capable, most expensive class of large language models produced by a handful of well-funded labs, and access to them is typically sold through APIs priced per token of input and output. In a commoditizing market, when several providers offer broadly comparable capability, buyers can switch relatively easily, which pushes vendors toward price competition instead of feature competition. This pattern has precedent in cloud computing and other infrastructure markets, where per-unit prices fall steadily as providers scale up and capacity grows.

**Tags**: `#AI industry`, `#pricing`, `#market analysis`, `#frontier models`, `#commoditization`

---

<a id="item-20"></a>
## [Raymond Chen Recounts the History of Windows Scroll Bar Shortcuts](https://devblogs.microsoft.com/oldnewthing/20260922-00/?p=112719/) ⭐️ 5.0/10

Raymond Chen published a new installment on his long-running 'The Old New Thing' Microsoft developer blog recounting the history of Windows scroll bar keyboard and mouse shortcuts. The post traces how these often-overlooked behaviors came to be defined in the Win32 era, prompting a fresh discussion about UI consistency in modern applications. The piece matters because most modern software no longer uses native Win32 scroll bars, so the carefully designed behaviors Chen describes are frequently lost or reimplemented inconsistently by UI frameworks. It is a concrete example of how platform-level interaction conventions erode as developers move to cross-platform toolkits and custom web components, affecting everyone who relies on predictable scrolling behavior. The article is a historical deep-dive rather than an announcement of new functionality, and it focuses on the semantics of interacting with the scroll bar gutter, buttons and thumb rather than on any single shortcut. The comment thread extends the topic beyond Windows by cataloguing how GTK and other Linux toolkits handle the same gestures, showing that the conventions are neither universal nor consistent.

hackernews · tybulewicz · Sep 23, 18:02 · [Discussion](https://news.ycombinator.com/item?id=49820065)

**Background**: Raymond Chen has worked on Windows for more than 30 years and his blog 'The Old New Thing' is well known for explaining the historical rationale behind Windows API and UI decisions. Scroll bars are a core part of the Win32 common controls, and because they were provided by the operating system, applications using them shared an identical look and interaction model. Today most applications instead use framework-provided or JavaScript-based scroll bars, such as overlayscrollbars, perfect-scrollbar and simplebar, which replace the native browser scroll bar with a customizable but functionally reduced version.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/oldnewthing/author/oldnewthing">Raymond Chen, Author at The Old New Thing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Raymond_Chen_(Microsoft)">Microsoft Developer Network - Wikipedia</a></li>
<li><a href="https://npm-compare.com/overlayscrollbars,perfect-scrollbar,simplebar">perfect-scrollbar vs overlayscrollbars vs simplebar | Custom ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed that the loss of native scroll bars is a regression: bartread lamented that framework scroll bars 'behave differently or do less', while layer8 wished Chen would more openly criticize today's UI inconsistencies. mrob argued that clicking a scroll bar should by default mean 'scroll here' since that action cannot be replicated by a keyboard shortcut, noting GTK gets this right and Qt does not, and butz and chrismorgan added practical notes on thin or hidden scroll bars, the Firefox layout.css.scrollbar-width-thin.disabled setting, and the varied Shift-click and middle-click behaviors across GTK, Firefox, LibreOffice and Inkscape.

**Tags**: `#Windows`, `#UI/UX`, `#scrollbars`, `#history`, `#Hacker News`

---

<a id="item-21"></a>
## [Data centres swap copper for light-based networking to cut power](https://www.bbc.co.uk/news/articles/c2dwg3zexkpo?at_medium=RSS&at_campaign=rss) ⭐️ 5.0/10

Data centres are beginning to replace copper wiring with optical (light-based) interconnects in order to reduce power consumption and increase network capacity, according to a BBC report. The shift moves signal transmission inside and between racks from electrical signals over copper to light travelling through fibre and silicon-photonic components. Power and cooling are now among the biggest constraints on data centre expansion, especially as AI training and inference workloads push bandwidth and energy demands sharply higher. If optical links can deliver more bandwidth per watt, they could ease the electricity bottleneck for hyperscale operators and reshape the supply chain for networking hardware. Optical interconnects transmit signals within and between chips and boards using light rather than electrical current, and silicon photonics allows these optical components to be fabricated with existing semiconductor techniques so that optics and electronics can be integrated on the same chip. The main trade-offs historically have been cost, laser reliability and the difficulty of packaging photonic components alongside high-volume silicon electronics.

rss · BBC Business · Sep 22, 23:03

**Background**: Copper has long been the default medium for short-reach networking inside data centres, but electrical signals suffer higher loss and consume more energy as speeds rise. Optical interconnect is a method of sending signals from one part of a circuit to another using light, typically over fibre optics. Silicon photonics applies photonic systems that use silicon as the optical medium, usually operating in the infrared around the 1.55 micrometre wavelength used by most telecom fibre systems, and is being researched by companies such as Intel and IBM as a way to keep pace with Moore's Law.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optical_interconnect">Optical interconnect</a></li>
<li><a href="https://en.wikipedia.org/wiki/Silicon_photonics">Silicon photonics</a></li>
<li><a href="https://www.intel.com/content/www/us/en/products/details/network-io/silicon-photonics.html">Intel® Silicon Photonics</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#optical interconnects`, `#energy efficiency`, `#networking`, `#silicon photonics`

---

<a id="item-22"></a>
## [BBC Reports China Building Dozens of Data Centres in Inner Mongolia for AI](https://www.bbc.co.uk/news/articles/cm5ydz4kl65ro?at_medium=RSS&at_campaign=rss) ⭐️ 5.0/10

The BBC reported from Inner Mongolia that dozens of Chinese data centres are currently under construction there, framing the region as an unlikely frontier in Beijing's artificial intelligence competition with Washington. The report describes the buildout as part of China's stated aim to lead the world in AI. It highlights that the AI race is increasingly a contest over physical infrastructure and compute capacity, not just models or algorithms, and that China is investing at a scale and pace meant to offset constraints on access to advanced chips. This matters to anyone tracking AI supply chains, energy demand, and the geopolitics of computing power. The available material is limited to a headline and a one-line teaser from the BBC's RSS feed, so it does not include figures on investment, capacity in megawatts or racks, chip types, operators, or completion dates. As a result, the specific technical scale and the mix of domestic versus imported hardware remain unverified from this item alone.

rss · BBC World · Sep 22, 22:04

**Background**: Data centres require large amounts of electricity and cooling, so they are often sited where power is cheap, land is abundant, and the climate is cool — conditions that fit Inner Mongolia, a major coal- and wind-power producing region in northern China. China has promoted a national 'East Data, West Computing' effort to move compute-intensive workloads from wealthy coastal cities to western regions with cheaper energy. Meanwhile, US export controls have restricted China's access to the most advanced AI chips, pushing Beijing to emphasise domestic alternatives and self-reliance in AI infrastructure. The headline is therefore part of a broader story about where and how AI compute gets built.

**Tags**: `#AI infrastructure`, `#data centers`, `#China`, `#geopolitics`, `#compute`

---