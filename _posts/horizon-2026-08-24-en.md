# Horizon Daily - 2026-08-24

> From 160 items, 18 important content pieces were selected

---

1. [MS Paint and Photos silently embed invisible GUID watermarks in AI-edited images](#item-1) ⭐️ 9.0/10
2. [seL4 Security Proofs Completed on AArch64](#item-2) ⭐️ 9.0/10
3. [IPFS Maintainers Winding Down](#item-3) ⭐️ 8.0/10
4. [Paul Graham: If I Were 17, I'd Build LLMs From Scratch](#item-4) ⭐️ 8.0/10
5. [AI Reliance Will Collapse Coding Expertise](#item-5) ⭐️ 8.0/10
6. [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](#item-6) ⭐️ 7.0/10
7. [Browser Game Recreates Entire San Francisco, Sparks Nostalgia and Debate](#item-7) ⭐️ 7.0/10
8. [How EU Rules Are Killing Makers and Micro-Entrepreneurs](#item-8) ⭐️ 7.0/10
9. [OpenAI Slashes GPT-5.6 Sol API Prices by Up to 33% Until Nov 21](#item-9) ⭐️ 7.0/10
10. [Nvidia says Groq racks will be online this year after $20 billion purchase](#item-10) ⭐️ 7.0/10
11. [XMPP at 25: Digital Independence vs. Adoption Struggles](#item-11) ⭐️ 6.0/10
12. [GlassBox Shows How Browser Fingerprinting Identifies You](#item-12) ⭐️ 6.0/10
13. [Zillow Settles FTC Claims It Paid Redfin to Stop Competing on Apartment Listings](#item-13) ⭐️ 6.0/10
14. [New Zealand proposes social media ban for under-16s](#item-14) ⭐️ 6.0/10
15. [Albanese moves to calm states over datacentre rules as power demand set to surge](#item-15) ⭐️ 6.0/10
16. [Goldman Sachs Partner Warns AI Could Weaken Bankers' Reasoning Skills](#item-16) ⭐️ 5.0/10
17. [Alibaba shares plunge 10% on $10.2 billion AI share placement](#item-17) ⭐️ 5.0/10
18. [UK to use Ukraine battlefield data to train AI for site protection](#item-18) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [MS Paint and Photos silently embed invisible GUID watermarks in AI-edited images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 9.0/10

Microsoft's Paint and Photos apps now silently embed an invisible GUID watermark into images that have been AI-manipulated, even when the AI processing runs locally on the user's device. The watermark is added in the background without user notification and cannot be turned off. This directly threatens user anonymity because the GUID can be traced back to a Microsoft account, potentially exposing personal identity if the image is shared. It also signals a growing trend of silent, embedded tracking features in consumer software that users cannot opt out of. The invisible watermark is separate from the optional visible AI-generated-content label, and it is embedded even when AI models run purely locally. Community reports indicate the watermark can trigger incorrectly during simple operations like resizing screenshots, and Microsoft has previously been sloppy with Copilot-related watermarking features.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: An invisible watermark is a signal embedded in an image that is imperceptible to the human eye but can be detected by software to identify the content's origin or owner. A GUID (Globally Unique Identifier) is a 128-bit number used by Microsoft to uniquely identify objects, and can be linked to a user account. AI watermarking methods, such as embedding signals during model training, are increasingly used by companies to trace AI-generated content back to its creator or the specific model that produced it.

<details><summary>References</summary>
<ul>
<li><a href="https://www.imatag.com/digital-watermarking">Invisible Digital Watermarking | The smart way to protect your online content</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchenterpriseai/definition/AI-watermarking">What is AI watermarking and how does it work?</a></li>

</ul>
</details>

**Discussion**: Commenters are highly concerned about the privacy implications, arguing that the real problem is the secret unique identifier, not the AI watermarking per se. Some recommend avoiding Windows and Microsoft AI-enabled apps entirely, citing Microsoft's past failures with Copilot watermarking and a report of a false trigger during a simple screenshot resize.

**Tags**: `#privacy`, `#watermarking`, `#Microsoft`, `#security`, `#AI`

---

<a id="item-2"></a>
## [seL4 Security Proofs Completed on AArch64](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 9.0/10

The seL4 microkernel's formal security proofs have been completed for the AArch64 (ARM64) architecture, announced by Proofcraft on August 21, 2026. This marks a major milestone in formally verifying an operating system kernel on a 64-bit ARM platform. This is significant because seL4 is the first operating system kernel with a formal proof of security properties, and extending it to AArch64—the architecture powering most smartphones and many embedded devices—broadens its applicability. It could accelerate adoption of formally verified kernels in security-critical systems such as automotive, avionics, and defense. The proof is limited to non-MCS (mixed-criticality system) configurations and single-core (unicore) execution, as noted in the fine print. Formal verification proves correctness against a specification but does not account for side-channel timing attacks or hardware vulnerabilities.

hackernews · snvzz · Aug 24, 11:32 · [Discussion](https://news.ycombinator.com/item?id=49418255)

**Background**: seL4 is a third-generation L4 microkernel developed by NICTA (now part of CSIRO) with the goal of providing a basis for highly secure and reliable systems. Formal verification uses mathematical methods to prove that a system satisfies its specification. AArch64, also known as ARM64, is the 64-bit instruction set architecture introduced with ARMv8-A and is widely used in mobile and embedded devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SeL4">seL4 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AArch64">AArch64 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the real-world impact, with one predicting a side-channel timing attack would invalidate the result and another pointing out the proof's restrictions to non-MCS and single-core configurations. Others discussed actual seL4 deployments, asking about operating systems and private uses, while one argued that without a native seL4/Linux, the capability model won't meaningfully improve system security.

**Tags**: `#seL4`, `#formal verification`, `#operating systems`, `#security`, `#AArch64`

---

<a id="item-3"></a>
## [IPFS Maintainers Winding Down](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 8.0/10

IPFS maintainers announce winding down of the project at Shipyard, prompting community reflection on the state of decentralized web technologies.

hackernews · iand · Aug 24, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49421489)

**Tags**: `#IPFS`, `#decentralized web`, `#p2p`, `#open source`, `#protocol labs`

---

<a id="item-4"></a>
## [Paul Graham: If I Were 17, I'd Build LLMs From Scratch](https://twitter.com/paulg/status/2091544343589060625) ⭐️ 8.0/10

Paul Graham tweeted that if he were 17, he would learn to build large language models from scratch. The post, published on X, sparked a wide-ranging discussion rather than announcing a technical result. As a prominent Silicon Valley investor and essayist, Graham's advice can shape how young people choose what to learn. The ensuing debate highlights a growing tension between deep theoretical knowledge and the practical reality of an LLM job market where few companies do real training. The original post is short and provides no specifics; its significance comes from the conversation it generated. Community commenters debated the feasibility of 'building LLMs from scratch' given the enormous compute and data budgets involved, and questioned whether advice from successful figures suffers from survivorship bias.

hackernews · bilsbie · Aug 23, 20:38 · [Discussion](https://news.ycombinator.com/item?id=49412396)

**Background**: Large language models are built on the transformer architecture introduced in the 2017 paper 'Attention Is All You Need'. Transformers use multi-head attention mechanisms to process token sequences in parallel, and building one from scratch typically means implementing tokenization, embeddings, attention layers, and training loops yourself. This background helps explain why Graham's advice is both inspiring and intimidating for a 17-year-old.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_architecture">Transformer architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Attention_(machine_learning)">Attention (machine learning) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/attention-mechanism">What is an attention mechanism? | IBM</a></li>

</ul>
</details>

**Discussion**: Comments were mixed. Some agreed that deeply understanding LLM internals builds valuable intuition and helps judge when 'just use an LLM' is the wrong approach. Others argued that real LLM training positions are rare, training costs are prohibitive for most, and advice from wealthy successful people may reflect survivorship bias. Several readers shared that they learn LLM internals purely out of fascination, not career utility.

**Tags**: `#LLM`, `#education`, `#machine learning`, `#career advice`

---

<a id="item-5"></a>
## [AI Reliance Will Collapse Coding Expertise](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 8.0/10

An article on Lars Faye's site argues that reliance on AI coding assistants prevents developers, especially juniors, from building deep expertise, predicting a collapse in coding proficiency. The piece sparked substantial community discussion, with 271 points and 311 comments on Hacker News. This matters because it challenges the current industry trend of maximizing AI-assisted coding speed, highlighting a potential erosion of core software engineering skills. If true, it could lead to a future workforce unable to reason about complex systems, with serious implications for software quality and maintainability. The article was scored 8.0/10 and attracted 271 points and 311 comments on Hacker News, indicating high engagement. Community commenters shared personal experiences of skill atrophy and criticized enterprise mandates that pressure engineers to rely on AI-generated code, which they say exceeds the pace of human review.

hackernews · larsfaye · Aug 24, 15:52 · [Discussion](https://news.ycombinator.com/item?id=49421554)

**Background**: AI coding assistants are large language model-based tools that generate source code from natural-language prompts, a practice often called 'vibe coding' when developers accept generated code without deep review. This approach has been praised for lowering barriers to programming, but critics warn of maintainability and security risks. Another relevant concept is automation bias, the tendency for humans to overtrust automated outputs, which in software engineering can lead engineers to accept flawed AI code without adequate scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automation_bias">Automation bias - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchitoperations/definition/What-is-automation-bias">What is Automation Bias? How to Avoid its Pitfalls | Informa TechTarget</a></li>

</ul>
</details>

**Discussion**: The overall sentiment in the comments is one of concern and agreement. Several developers recounted personal experiences of skill atrophy and gave mixed reactions to pressure from management to use AI. Some argued that the best engineers actively seek friction and will still develop deep expertise, but others warned of a 'snake eating its own tail' dynamic where AI-generated code degrades the abilities of those who have to maintain it.

**Tags**: `#AI coding`, `#software engineering`, `#developer expertise`, `#LLM impact`, `#skill atrophy`

---

<a id="item-6"></a>
## [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

Xiaomi's new CPU reportedly matches Apple's single-threaded performance and leads in multithreading, but power consumption and real-world phone performance remain key concerns.

hackernews · tosh · Aug 24, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49420873)

**Tags**: `#CPU`, `#Xiaomi`, `#Apple`, `#ARM`, `#benchmarking`

---

<a id="item-7"></a>
## [Browser Game Recreates Entire San Francisco, Sparks Nostalgia and Debate](https://sf.thijs.gg/) ⭐️ 7.0/10

A browser-based game at sf.thijs.gg recreates all of San Francisco in 3D using WebGL. Users can explore the city on foot, sparking wide interest within hours of appearing on Hacker News. The project demonstrates that an entire real-world city can be rendered interactively in a web browser without plugins, pointing toward a future of lightweight, accessible virtual tourism and urban simulation. Its emotional resonance for former residents shows how game technology can connect people with familiar places in new ways. Built with WebGL, the page reportedly consumes about 400 MB on load and grows to roughly 2 GB after several minutes, suggesting memory leaks that cause the scene to degrade into blobs. The scope is limited to walking gameplay, with no stated goal beyond exploration, and popular landmarks such as Alcatraz are accessible.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: WebGL is a JavaScript API for rendering interactive 2D and 3D graphics in web browsers without plug-ins, based on OpenGL ES. Procedural generation is a method of creating data algorithmically rather than manually, commonly used in games to build worlds. This project combines these techniques to stream an entire city into the browser.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGL">WebGL - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API">WebGL: 2D and 3D graphics for the web - Web APIs | MDN</a></li>
<li><a href="https://en.wikipedia.org/wiki/Procedural_generation">Procedural generation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters shared strong emotional responses, with one former 20-year resident saying the recreation made them emotional while revisiting old haunts. Others reported fun exploring, but also noted technical issues: one user on an M3 Air saw memory usage climb from 400 MB to 2 GB before the scene degraded. A few commenters compared it to Watch Dogs 2 and Microsoft Flight Simulator's take on San Francisco.

**Tags**: `#WebGL`, `#3D rendering`, `#Browser game`, `#San Francisco`, `#Demo`

---

<a id="item-8"></a>
## [How EU Rules Are Killing Makers and Micro-Entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) ⭐️ 7.0/10

An opinion piece argues that recent EU regulations such as the PPWR packaging rule and the WEEE e-waste directive disproportionately burden makers and micro-entrepreneurs, calling the compliance demands unsustainable. The debate matters because it exposes a growing conflict between EU environmental policy and the small-scale maker economy, potentially stifling innovation and new business creation. If unaddressed, the compliance burden could push European micro-entrepreneurs out of the market or out of the EU. The PPWR (Regulation (EU) 2025/40) entered into force on 11 February 2025, replacing the old packaging directive, while the WEEE directive already governs e-waste recycling. Commenters note that unlike VAT, most regulations still require separate filings in each EU member state, creating near-impossible administrative burdens for small sellers.

hackernews · l-one-lone · Aug 24, 13:05 · [Discussion](https://news.ycombinator.com/item?id=49419237)

**Background**: PPWR is a new EU regulation that aims to make all packaging recyclable and increase recycled content, applying to everything sold on the EU market. WEEE is a directive that requires producers of electrical and electronic equipment to fund collection and recycling systems. Makers and micro-entrepreneurs typically sell small volumes of niche products, so fixed compliance costs per item are disproportionately high. The article argues that this makes EU regulations written for large corporations particularly harmful to small businesses.

<details><summary>References</summary>
<ul>
<li><a href="https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste/packaging-packaging-waste-regulation_en">Packaging Waste Regulation - EU Environment</a></li>
<li><a href="https://www.business.gov.uk/campaign/europe/european-union-eu-regulations/eu-packaging-and-packaging-waste-regulation-eu-ppwr/">EU PPWR – Packaging and Packaging Waste Regulation</a></li>
<li><a href="https://deutsche-recycling.com/weee-eu-directive/">WEEE EU Directive : Electrical Waste Management Guide</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree with the article, sharing personal frustrations with EU bureaucracy. They cite aggressive Spanish tax enforcement, fragmented national adoption of EU rules, and the impossibility of submitting separate reports for every country. Some contrast China's centralized logistics choke points and phased rollouts, while others argue the admin costs outweigh any environmental benefit.

**Tags**: `#EU regulation`, `#entrepreneurship`, `#makers`, `#policy`, `#small business`

---

<a id="item-9"></a>
## [OpenAI Slashes GPT-5.6 Sol API Prices by Up to 33% Until Nov 21](https://developers.openai.com/api/docs/pricing) ⭐️ 7.0/10

OpenAI announced a temporary price reduction for its flagship GPT-5.6 Sol API, cutting input token prices by 20% and output token prices by 33%. The discounted pricing is guaranteed through at least November 21, 2026. This price cut intensifies the ongoing AI API price war, as model distillation and commoditization erode the moats of frontier labs. Developers and startups stand to benefit from lower costs, while competitors like Anthropic may face pressure to match pricing. The new per-million-token pricing for gpt-5.6-sol is $4.00 for input, $0.40 for cached input, $5.00 for cache writes, and $20.00 for output. Despite the discount, Sol remains 20 times more expensive than the Luna variant, but it is now more competitive with Anthropic's offerings.

hackernews · tosh · Aug 24, 15:22 · [Discussion](https://news.ycombinator.com/item?id=49421074)

**Background**: GPT-5.6 is a family of large language models from OpenAI, released on July 9, 2026, with three variants: Luna, Terra, and Sol, ranked from least to most capable. Sol is the flagship model designed for maximum capability. AI model distillation is a technique where a large 'teacher' model transfers its knowledge to a smaller 'student' model, often reducing size by 5 to 50 times, which makes replication easier and drives down the cost of AI intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>
<li><a href="https://www.linkedin.com/posts/danharper_openais-gpt-56-sol-is-the-best-thing-to-activity-7487627892898791425-9aIB">OpenAI's GPT 5 . 6 Sol is the best thing to happen to open models..</a></li>
<li><a href="https://medium.com/@creed_1732/5-powerful-ways-ai-model-distillation-is-revolutionizing-affordable-machine-learning-and-why-its-c239cc039b63">5 Powerful Ways AI Model Distillation Is Revolutionizing... | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters on the pricing news debated whether easy distillation prevents an AI monopoly and could turn intelligence into a race to the bottom. Some welcomed the price war and praised open-source models, while others compared Sol's new pricing with Anthropic and speculated about switching from Claude Fable to Codex.

**Tags**: `#OpenAI`, `#GPT-5`, `#Pricing`, `#AI API`, `#Competition`

---

<a id="item-10"></a>
## [Nvidia says Groq racks will be online this year after $20 billion purchase](https://www.cnbc.com/2026/08/24/nvidia-says-groq-racks-will-be-online-this-year-after-20-billion-deal.html) ⭐️ 7.0/10

In August 2026, Nvidia said that after completing its $20 billion acquisition of Groq, it plans to bring Groq racks online to customers this year. The announcement underscores Nvidia's push to make Groq's low-latency inference chips commercially available quickly. This gives Nvidia a new ASIC-based product line specifically aimed at low-latency inference, an area where GPUs may not be the most efficient option. It is a major signal for the AI industry that inference speed and cost are becoming as important as training capability, potentially reshaping the AI hardware market. Groq designs an application-specific integrated circuit (ASIC) called the Language Processing Unit (LPU), which is built for inference rather than model training. The public announcement is a brief news item and does not disclose specific rack configurations, timelines, or performance targets.

rss · CNBC Top News · Aug 24, 17:19

**Background**: Low-latency AI inference means an AI model can process a request and return a result in milliseconds or even microseconds, which is critical for real-time interactive applications. Groq's core bet has been that inference would become the dominant cost in AI and that a chip specialized for inference would be better suited than a training-focused GPU. Nvidia's $20 billion acquisition and plan to bring Groq racks online this year highlight how the industry is pivoting toward inference efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://www.voiceflow.com/blog/groq">Groq AI : LPU Chips , GroqCloud, and Pricing (2026)</a></li>
<li><a href="https://www.siliconflow.com/articles/en/the-lowest-latency-inference-api">Ultimate Guide – The Best Lowest Latency Inference APIs of 2026</a></li>

</ul>
</details>

**Tags**: `#AI`, `#hardware`, `#acquisition`, `#inference`, `#Nvidia`

---

<a id="item-11"></a>
## [XMPP at 25: Digital Independence vs. Adoption Struggles](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 6.0/10

A retrospective blog post by Gultsch commemorates 25 years of Jabber/XMPP, reflecting on its role in digital independence while acknowledging adoption challenges. The accompanying Hacker News discussion compares XMPP's federated architecture with newer protocols like Matrix. XMPP remains one of the oldest open messaging standards and a cornerstone of federated communication, showing that decentralized chat can survive without corporate backing. The debate highlights ongoing tensions between protocol maturity, user adoption, and modern feature demands in the messaging ecosystem. XMPP, originally named Jabber, is an XML-based protocol formalized as an open standard in 2004, with a federated server model similar to email. Critics note its fragmented client ecosystem and stalled consumer adoption compared to Matrix, which offers JSON-based messaging, HTTP APIs, and WebRTC integration but has faced vendor lock-in concerns.

hackernews · inputmice · Aug 24, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49421536)

**Background**: XMPP (Extensible Messaging and Presence Protocol) was developed by the open-source community in 1999 and quickly became the foundation for many early instant messaging services; by 2003 it was used by over ten million people. Matrix is a newer open standard for real-time communication that also supports federated messaging, but it was built independently rather than extending XMPP. The retrospective appears on gultsch.de, the blog of an XMPP developer, and the discussion reflects ongoing debates in the open-source communication community.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XMPP_protocol">XMPP protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matrix_(protocol)">Matrix (protocol)</a></li>
<li><a href="https://selfhosting.sh/compare/matrix-vs-xmpp/">Matrix vs XMPP : Federated Chat Protocols Compared | selfhosting.sh</a></li>

</ul>
</details>

**Discussion**: Commenters expressed affection for XMPP, praising its longevity and resilience, yet acknowledged that adoption remains the biggest hurdle. Several lamented that Matrix 'reinvented the wheel' instead of improving XMPP, speculating about what funding could have accomplished, while others questioned whether any major communities still use Jabber today.

**Tags**: `#XMPP`, `#Jabber`, `#instant messaging`, `#Matrix`, `#protocols`

---

<a id="item-12"></a>
## [GlassBox Shows How Browser Fingerprinting Identifies You](https://glassbox.codecanary.org/) ⭐️ 6.0/10

GlassBox is a new browser fingerprinting tool that shows visitors how uniquely identifiable their browser configuration is. It was posted on Hacker News as a 'Show HN' project, demonstrating the data browsers expose to websites. The tool highlights growing privacy concerns around browser fingerprinting, a technique used for tracking users even when cookies are blocked. It joins a crowded field of similar privacy-testing services, but the discussion it generated shows ongoing public interest in understanding digital identifiability. GlassBox is hosted at glassbox.codecanary.org and functions like existing tools such as EFF's Cover Your Tracks, which also reveal browser fingerprint uniqueness. Commenters noted that the site's language appears AI-generated, and that the project resembles a previous similar submission.

hackernews · tke248 · Aug 24, 16:15 · [Discussion](https://news.ycombinator.com/item?id=49421948)

**Background**: Browser fingerprinting is the collection of software and hardware information from a remote device to identify it, typically producing a short identifier via a fingerprinting algorithm. Websites can use this to track users even when cookies are disabled or IP addresses are hidden, which raises significant privacy concerns. Services like GlassBox let users see how unique their own fingerprint is and therefore how easily they could be tracked.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Browser_fingerprinting">Browser fingerprinting</a></li>

</ul>
</details>

**Discussion**: The comment section points to existing alternatives like EFF's Cover Your Tracks and notes that a similar tool was posted weeks earlier. Some users expressed unease about how much data browsers expose, while others criticized the site's AI-sounding copy. One commenter added nuance by explaining that both uniqueness and stability are needed for a fingerprint to be a tracking identity.

**Tags**: `#privacy`, `#browser fingerprinting`, `#web tracking`, `#security`

---

<a id="item-13"></a>
## [Zillow Settles FTC Claims It Paid Redfin to Stop Competing on Apartment Listings](https://www.cnbc.com/2026/08/24/zillow-settles-ftc-claims-it-paid-redfin-to-stop-competing-on-listings.html) ⭐️ 6.0/10

Zillow has settled Federal Trade Commission claims that it paid Redfin to stop competing on apartment listings, avoiding a trial that was set to begin Monday. Regulators argued the partnership drove up costs for landlords and degraded listing quality. The settlement signals continued antitrust scrutiny of large tech platforms using payments to sideline rivals, potentially reshaping how real estate marketplaces structure partnerships. It matters for landlords, renters, and the broader online listings industry because such agreements can reduce competition and harm consumers. The FTC and state attorneys general were prepared to argue at trial that the Zillow-Redfin partnership raised costs for landlords and decreased listing quality. The exact settlement terms, including any fines or conduct restrictions, have not been detailed in the available information.

rss · CNBC Top News · Aug 24, 15:35

**Background**: Zillow is a major online real estate and rental marketplace, while Redfin is a real estate brokerage that also operates a listings platform. The FTC enforces U.S. antitrust law, including rules against agreements that reduce competition. At issue was an alleged arrangement in which Zillow paid Redfin not to compete in apartment listings, a type of horizontal restraint that can lead to higher prices and lower quality for consumers.

**Tags**: `#antitrust`, `#real estate`, `#tech industry`, `#regulation`, `#Zillow`

---

<a id="item-14"></a>
## [New Zealand proposes social media ban for under-16s](https://www.theguardian.com/media/2026/aug/24/nz-social-media-ban-children-under-16-fines-meta-tiktok) ⭐️ 6.0/10

New Zealand's prime minister, Christopher Luxon, announced his party will introduce a bill to ban children under 16 from using social media. Platforms that fail to comply could face fines of up to 10% of global annual revenue. The proposed legislation is a major regulatory push that would directly affect major platforms such as Meta and TikTok. It also signals a growing trend of government intervention in children's online safety and could spur adoption of age verification technologies. The bill would require social media platforms to take reasonable steps to verify users' ages, using existing account information, facial age estimation, and digital identity documents. Fines for non-compliance could reach 10% of a platform's global revenue.

rss · The Guardian World · Aug 24, 05:22

**Background**: Age verification on social media is technically challenging, as platforms must balance user privacy with the need to confirm ages. Common approaches include facial age estimation technologies, which analyze facial landmarks to estimate age, and digital identity documents that users can present online. These tools are increasingly being adopted by companies such as Yoti and are supported by identity-provider services like Google's digital ID feature.

<details><summary>References</summary>
<ul>
<li><a href="https://www.yoti.com/business/age-verification/">Age checks for online users and custom-built apps - Yoti</a></li>
<li><a href="https://support.google.com/accounts/answer/10071085?hl=en">Access age -restricted content & features - Google Account Help</a></li>

</ul>
</details>

**Tags**: `#social media`, `#regulation`, `#New Zealand`, `#age verification`, `#policy`

---

<a id="item-15"></a>
## [Albanese moves to calm states over datacentre rules as power demand set to surge](https://www.theguardian.com/australia-news/2026/aug/25/albanese-seeks-to-quell-datacentre-disquiet-as-climate-expert-warns-weve-got-one-shot-to-get-the-rules-right) ⭐️ 6.0/10

Prime Minister Anthony Albanese will use Wednesday's national cabinet meeting to reassure premiers that new national controls on datacentre developments will complement state rules. He also announced plans for major AI legislation next year, following AEMO's forecast of a seven-fold rise in datacentre power use. This marks a pivotal moment in Australia's attempt to balance the economic benefits of the AI boom with climate commitments. The outcome will shape where and how datacentres are built, affecting both the clean energy transition and the nation's digital competitiveness. The federal plans face opposition from conservative governments in Queensland and the Northern Territory, which fear federal overreach. A climate expert warned that 'we've got one shot to get the rules right,' underscoring the stakes for long-term energy planning.

rss · The Guardian World · Aug 24, 14:01

**Background**: AEMO, the Australian Energy Market Operator, manages the National Electricity Market and is responsible for national transmission planning. Datacentres are highly energy-intensive, and the AI boom is driving rapid growth in their electricity demand. The Australian government is also establishing an Office of AI within the Department of Prime Minister and Cabinet to oversee AI regulation and data centre rules.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AEMO">AEMO</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pPbXFMQ0VSRVphREdCcGJjSWhTZ0FQAQ?hl=en-US&gl=US&ceid=US:en">Google News - Anthony Albanese to establish a new Office of AI ...</a></li>

</ul>
</details>

**Tags**: `#datacentre`, `#AI regulation`, `#energy policy`, `#Australia`, `#climate`

---

<a id="item-16"></a>
## [Goldman Sachs Partner Warns AI Could Weaken Bankers' Reasoning Skills](https://www.cnbc.com/2026/08/24/goldman-sachs-ai-partner-danger-skills.html) ⭐️ 5.0/10

A Goldman Sachs partner has issued a warning that the bank's aggressive adoption of AI carries an unintended risk: eroding the reasoning skills of future bankers. The caution highlights a tension between efficiency gains from automation and the preservation of core human analytical abilities. This matters because AI is being rapidly integrated into high-stakes financial decision-making, and if junior staff rely on AI without developing their own judgment, the industry could face a systemic skills gap. It also adds to a growing debate about the long-term impact of AI on professional expertise and workforce development. The warning specifically targets the erosion of reasoning skills rather than job losses, suggesting that the risk is not only about headcount but about the quality of future decision-making. No official policy changes or technical details were provided in the report.

rss · CNBC Top News · Aug 24, 15:50

**Background**: Many financial institutions, including Goldman Sachs, are deploying AI tools for tasks such as data analysis, report generation, and routine operational work. While these tools can boost productivity, there is concern that over-reliance on them may cause younger professionals to lose the deep analytical and critical-thinking skills traditionally built through hands-on experience. The debate reflects a broader industry tension between adopting transformative technology and preserving human expertise.

**Tags**: `#AI`, `#Finance`, `#Reasoning`, `#Risk`, `#Workforce`

---

<a id="item-17"></a>
## [Alibaba shares plunge 10% on $10.2 billion AI share placement](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 5.0/10

Alibaba priced a $10.2 billion share placement to fund its AI initiatives, causing its Hong Kong-listed shares to plunge about 10%. This is one of Alibaba's largest equity raises and underscores the escalating AI arms race among Chinese tech giants. The sharp sell-off shows investors are wary of heavy dilution and the high costs required to compete in AI. The placement was priced at a discount to the market price, a common feature of such deals that often pressures the stock. Alibaba has recently increased spending on AI infrastructure and cloud computing, while facing regulatory and macroeconomic uncertainties.

rss · CNBC Top News · Aug 24, 08:21

**Background**: A share placement is a way for listed companies to raise capital quickly by selling new shares to selected institutional investors, but it dilutes existing shareholders. Alibaba's move fits a broader pattern of Chinese tech companies pivoting to AI after several years of strict regulatory scrutiny, though the outcome remains uncertain.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=33869101">I'm a fan of Superstonk Out of curiosity, why is that? | Hacker News</a></li>
<li><a href="https://www.bajajfinserv.in/videos/why-companies-issue-shares">Why / Companies / Issue / Shares /|/Bajaj/Finance</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#AI investments`, `#share placement`, `#stock market`, `#tech industry`

---

<a id="item-18"></a>
## [UK to use Ukraine battlefield data to train AI for site protection](https://www.theguardian.com/politics/2026/aug/24/uk-to-use-ukraine-battlefield-data-to-train-ai-to-protect-sensitive-sites) ⭐️ 5.0/10

The UK and Ukraine have signed a deal granting the UK access to Ukraine's Avengers AI Labs database, which contains five million annotated battlefield images, to train AI models for protecting UK defence sites, railways and energy plants. Private companies will also be granted access to the data to develop new systems, marking the first such agreement in the UK. This is the first agreement of its kind in the UK, applying real-world battlefield data to the protection of national critical infrastructure. It signals a growing trend of using AI in defence and security and deepens UK-Ukraine technological cooperation. The database was compiled from thousands of daylight cameras and infrared sensors across the Ukrainian battlefield, providing operational experience that no laboratory simulation can replicate. The deal was signed by President Volodymyr Zelenskyy and Prime Minister Andy Burnham, with the UK becoming the first international partner granted entry to the Avengers AI Labs.

rss · The Guardian World · Aug 24, 18:16

**Background**: Ukraine's Avengers AI Labs is a platform that collects and annotates battlefield imagery to train AI models for military purposes. The dataset is considered uniquely valuable because real-world combat conditions are far more complex and unpredictable than simulated environments. The UK and Ukraine have been deepening defence links amid ongoing conflict, and this partnership formalises a new channel for sharing operational data. By granting private companies access, the UK also aims to stimulate innovation in AI-based security technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gov.uk/government/news/new-partnership-set-to-see-the-uk-and-ukraine-develop-battle-winning-technology-as-britain-secures-access-to-ukraines-avengers-ai-labs">New partnership set to see the UK and Ukraine develop... - GOV.UK</a></li>
<li><a href="https://www.planet-today.com/2026/08/uk-accesses-ukraine-avengers-ai-dataset.html">UK Accesses Ukraine Avengers AI Dataset: Battlefield Goldmine...</a></li>
<li><a href="https://www.manchestereveningnews.co.uk/news/world-news/uk-signs-ground-breaking-ai-34509786">UK signs 'ground-breaking' AI deal with Ukraine during Andy...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#defense`, `#critical infrastructure`, `#data sharing`, `#UK politics`

---

