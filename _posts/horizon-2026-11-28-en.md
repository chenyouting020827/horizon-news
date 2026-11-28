# Horizon Daily - 2026-11-28

> From 115 items, 14 important content pieces were selected

---

1. [State attorneys general sue SpaceX over Grok generating child sexual abuse material and revenge porn](#item-1) ⭐️ 8.0/10
2. [WebRTC-Based Card Skimming Scripts Found on Popular Shopping Sites Before Black Friday](#item-2) ⭐️ 7.0/10
3. [Show HN: bouncemarket, a live prediction market for a bouncing ball](#item-3) ⭐️ 7.0/10
4. [Rayshader 1.0: R's 3D Map Rendering Package Reaches Major Milestone](#item-4) ⭐️ 7.0/10
5. [Michael Nielsen Took Down His Free Neural Networks Book](#item-5) ⭐️ 7.0/10
6. [GitHub issue: Convex coding skill silently uploads user app ideas to remote server](#item-6) ⭐️ 6.0/10
7. [9/UX brings a Macintosh-inspired desktop to 9front](#item-7) ⭐️ 6.0/10
8. [Citroën's Hydraulic Suspension, Brakes and Steering Explained](#item-8) ⭐️ 6.0/10
9. [Show HN: DragDropMath Teaches Algebra Through Guardrailed Drag-and-Drop](#item-9) ⭐️ 6.0/10
10. [OpenAI Countersues Apple Over Alleged Trade Secret Theft](#item-10) ⭐️ 6.0/10
11. [Blog Post and HN Thread Trade Horror Stories of Legacy Version Control](#item-11) ⭐️ 5.0/10
12. [AT&T Unix PC (3B1) Emulator VM Gains Ethernet, TCP/IP and a 187-Package App Suite](#item-12) ⭐️ 5.0/10
13. [Anthropic Valued Like a Monopoly Despite Commodity-Like AI, Analyst Argues](#item-13) ⭐️ 5.0/10
14. [Fed Reportedly Worries About AI's Off-Balance-Sheet Financing](#item-14) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [State attorneys general sue SpaceX over Grok generating child sexual abuse material and revenge porn](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 8.0/10

A coalition of state attorneys general, led by Virginia's Jay Jones and Oregon's Dan Rayfield, filed suit against SpaceX — the parent company of X, xAI and Grok — over the creation and promotion of child sexual abuse material and non-consensual intimate images on the platform. The complaint targets Grok's image-generation capabilities and how the platform distributes the resulting content, rather than a single isolated output. This is one of the most significant state-level enforcement actions yet against a generative AI image model, and it tests whether a parent company can be held liable for the outputs of an AI product it owns. A ruling against SpaceX would set a precedent that could reshape content moderation requirements, model-level safeguards and liability allocation across the AI industry. The suit names the parent company rather than only the model developer, framing the harm as the creation and promotion of abusive imagery at the platform level — a legal structure other state AGs could copy in future filings. Grok's image generation is tied to X accounts, and the model family has previously drawn controversy over sexual deepfakes, which is likely to be central to the states' arguments.

hackernews · DeepLogin · Nov 27, 19:42 · [Discussion](https://news.ycombinator.com/item?id=50670855)

**Background**: Grok is the family of large language and image models developed by xAI, the Elon Musk-founded company launched in 2023 and integrated with the X social network; per public reporting, xAI became a subsidiary of SpaceX in early 2026, which is why the suit names SpaceX as the defendant. Grok has shipped several model generations with expanding capabilities including image generation, and has previously been criticized for generating sexualized deepfakes and other harmful content. Child sexual abuse material is illegal under both federal and state law, and non-consensual intimate imagery (often called "revenge porn") is similarly outlawed in most US states — but applying those rules to AI-generated output is legally novel.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot)</a></li>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">XAI (company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceXAI">SpaceXAI - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were unsure whether Grok's guardrails were simply extremely permissive or whether users had to deliberately trick it, suggesting confusion about how easily the content could be produced. Others argued the focus should shift to the individuals who requested the images, and one noted that because using Grok requires linking an X account, abusers face an identity trail that makes the behavior harder to explain away.

**Tags**: `#AI safety`, `#content moderation`, `#generative AI`, `#legal/regulation`, `#xAI`

---

<a id="item-2"></a>
## [WebRTC-Based Card Skimming Scripts Found on Popular Shopping Sites Before Black Friday](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

A credit-card skimming script was planted on the online stores of Lascana, Samsonite, American Tourister, Revolve and FWRD in the week before Black Friday, harvesting payment data from checkout pages. All of the sites contacted by the researchers took action after being notified. The campaign landed during the year's busiest online shopping period and shows that attackers are adopting less-monitored browser APIs to slip past security tooling and Content Security Policy filters. It underscores that any site embedding third-party scripts is exposed, regardless of how well its own code is written. Per the commenters, WebRTC is only an evasion vector rather than a root cause: the same exfiltration could be done with ordinary HTTP requests or a cross-domain POST, possibly because WebRTC endpoints were not listed in the sites' connect-src CSP directives or because the skimmer targeted mobile browsers that are harder to inspect.

hackernews · scanr · Nov 27, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50668145)

**Background**: WebRTC (Web Real-Time Communication) is a free, open-source browser API that lets pages send audio, video and arbitrary data directly between peers without plugins. Web skimming, also called digital skimming or Magecart-style attacks, works by injecting malicious JavaScript into ecommerce checkout pages so card details are copied as shoppers type them. Because most stores rely on third-party scripts for analytics, ads and chat widgets, a compromise anywhere in that supply chain can turn a trusted site into a data-theft channel.

<details><summary>References</summary>
<ul>
<li><a href="https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer">Credit card skimming scripts using WebRTC found on popular ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebRTC">WebRTC - Wikipedia</a></li>
<li><a href="https://noc.org/learn/credit-card-skimmers">Credit Card Skimmers | NOC.org</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread (413 points, 214 comments) largely pushes back on the headline framing: commenters argue WebRTC is merely less frequently monitored and that plain AJAX or cross-domain POSTs would work just as well, with one asking whether the sites simply forgot to add WebRTC to their connect-src CSP. The dominant sentiment is that third-party script embedding is the real vulnerability, with some users pointing to ad blockers as a legitimate defense and others questioning why the web lets strangers run arbitrary code or why payments still rely on symmetric secrets.

**Tags**: `#security`, `#web-security`, `#credit-card-skimming`, `#WebRTC`, `#third-party-scripts`

---

<a id="item-3"></a>
## [Show HN: bouncemarket, a live prediction market for a bouncing ball](https://bouncemarket.minhanhday.com/) ⭐️ 7.0/10

Developer Minh Anh Day launched bouncemarket, a browser game where a ball is dropped from a randomized starting position and players trade prediction-market shares on where it will land. The entire drop is simulated server-side and streamed to clients as server-sent events with a small buffer, so every round is deterministic and can be replayed exactly. The project is a compact, self-contained testbed for ideas that matter in real prediction markets: algorithmic market makers, arbitrage behavior, and whether human traders can beat bots. It also raises a live legal and conceptual question about whether markets on purely random events count as financial contracts rather than gambling. Because the outcome is deterministic from the starting position, a tiny change in that position can flip the final result, which means a precise solver could in principle compute the landing spot ahead of everyone else. The built-in AI traders use a naive hand-written rule set and drop out of any round with more than five human players, so the market only gets hard when it fills with real people.

hackernews · mday404 · Nov 27, 15:01 · [Discussion](https://news.ycombinator.com/item?id=50667726)

**Background**: A prediction market lets participants buy shares that pay out if a specific outcome occurs, and the share price acts as a crowd-sourced probability estimate. Server-sent events (SSE) is a standard HTTP mechanism for pushing a continuous stream of updates from a server to a browser over a single long-lived connection. "Deterministic" here means the physics simulation has no randomness of its own: identical inputs always produce identical results, which is what makes exact replay and third-party verification possible.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events">Using server - sent events - Web APIs | MDN</a></li>
<li><a href="https://antithesis.com/docs/resources/deterministic_simulation_testing/">Deterministic simulation testing - how it works and... | Antithesis Docs</a></li>

</ul>
</details>

**Discussion**: Commenters enjoyed the concept but flagged two problems: the drop resolves so fast that odds can swing from 0.01 to 0.99 in a tenth of a second, and simply buying cheap shares on both sides regardless of the ball is a profitable arbitrage. Others noted the game is effectively a bot-versus-bot contest once a frontier model is pointed at it, and one commenter wished someone would run a real-money version to test whether markets on pure randomness are legally treated as financial contracts.

**Tags**: `#prediction markets`, `#game`, `#simulation`, `#AI agents`, `#Show HN`

---

<a id="item-4"></a>
## [Rayshader 1.0: R's 3D Map Rendering Package Reaches Major Milestone](https://www.tylermw.com/posts/rayverse/rayshader-1-0-exit-the-matrix.html) ⭐️ 7.0/10

Rayshader, the open-source R package for building 2D and 3D hillshaded maps from elevation data, has shipped version 1.0, accompanied by a long technical release write-up titled "Exit the Matrix" on author Tyler Morgan-Wall's blog. The post covers new rendering capabilities along with related "rayverse" features that extend the package's visualization pipeline. Reaching 1.0 signals API stability for a package that has become a go-to tool for reproducible, publication-quality terrain and spatial visualization in the R ecosystem, where GIS and data-analysis workflows often lack a native path to 3D rendering. It matters most to R users in data journalism, geospatial analysis and academia who want 3D maps without leaving R for a separate graphics stack. Rayshader generates maps by treating elevation as a base R matrix and combining raytracing, hillshading, spherical texture mapping, ambient occlusion and overlays; it also includes a built-in path tracer, water detection and layering, programmable color palettes, Wavefront OBJ export and 3D-printable output. The specific feature list for 1.0 should be read from the release post itself, and the "Exit the Matrix" title appears to nod to the package's long-standing matrix-based elevation workflow.

hackernews · tylermw · Nov 27, 14:30 · [Discussion](https://news.ycombinator.com/item?id=50667371)

**Background**: Elevation data for terrain (such as digital elevation models from surveys or satellites) usually arrives as a grid of height values, which in R is naturally represented as a matrix, where each cell holds the altitude at a point. Rayshader takes such a matrix and renders it as a shaded surface: it computes surface normals, casts rays to simulate sunlight and shadow, and drapes color or imagery over the resulting relief. A "rayverse" is simply the family of related packages by the same author that build on this rendering core. Before tools like this, producing a good-looking 3D terrain rendering typically required dedicated GIS software or a separate 3D graphics engine.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rayshader.com/">Create Maps and Visualize Data in 2D and 3D • rayshader</a></li>
<li><a href="https://cran.r-project.org/web/packages/rayshader/rayshader.pdf">Package ‘rayshader’ - The Comprehensive R Archive Network I can rayshade, and so can you - GitHub Pages Beautiful shaded maps with rayshader Rayshader 1.0: Exit the Matrix – Tyler Morgan-Wall rayshader R package [Documentation] | R PACKAGES</a></li>

</ul>
</details>

**Discussion**: Sentiment is largely positive: one commenter, who says they know little R, called the package impressive and singled out the post's line about beauty being table stakes, while another shared their own pipeline that turns OpenStreetMap, USGS elevation and lidar data into an open-world Godot game and found the write-up helpful. The main pushback came from a skeptic who asked why anyone would use this rather than having an LLM one-shot the same result in Three.js or Raylib, a claim other readers would likely dispute; a minor bug report noted a broken bibliography video on iPad.

**Tags**: `#R`, `#data-visualization`, `#3D-rendering`, `#GIS`, `#open-source`

---

<a id="item-5"></a>
## [Michael Nielsen Took Down His Free Neural Networks Book](https://neuralnetworksanddeeplearning.com/) ⭐️ 7.0/10

Michael Nielsen removed his widely used free online book 'Neural Networks and Deep Learning' from neuralnetworksanddeeplearning.com, apparently as a statement about AI risk. The takedown triggered a 243-comment Hacker News thread, in which readers immediately posted Wayback Machine links and a consolidated PDF rebuilt with Typst. The book was one of the most recommended free starting points for people learning deep learning, so its removal affects a large population of self-taught practitioners, students, and course instructors. The episode also highlights a growing tension between the open-science norm of freely sharing ML knowledge and individual researchers' concerns about the risks of the technology they helped popularize. Because the text has been mirrored and archived many times, the practical effect of the takedown is limited: commenters linked a Wayback Machine snapshot and a CC BY-NC licensed PDF assembled from the archived site with Typst, noting that the interactive elements work worse than the original web version but remain usable as a reference. The book itself is an introductory text covering core ideas such as backpropagation, gradient descent, and convolutional networks rather than frontier research.

hackernews · brandonb · Nov 27, 19:31 · [Discussion](https://news.ycombinator.com/item?id=50670757)

**Background**: Michael Nielsen is a physicist and science writer known for work on quantum computing and open science, and 'Neural Networks and Deep Learning' was his free, web-native textbook introducing neural networks to beginners. Published in the mid-2010s, it became a standard recommendation in introductory ML discussions, in part because it explained concepts in plain language with runnable code. In recent years Nielsen has publicly expressed concern about existential risk from advanced AI, and removing his own educational material is a notable way of acting on that view.

**Discussion**: Commenters were split but largely critical of the move: one argued that helping people understand what big companies build behind closed doors better prepares society, comparing it to hiding the geology of subsidence from non-industry experts, while another accepted the intent but called it more of a protest than a practical act, since the book is mirrored everywhere and the removal may only increase demand. Others used the thread to argue that ASI-like capabilities have effectively already arrived, and several focused on practical archiving, sharing archive links and a Typst-built PDF.

**Tags**: `#deep-learning`, `#open-access`, `#ai-safety`, `#education`, `#community-discussion`

---

<a id="item-6"></a>
## [GitHub issue: Convex coding skill silently uploads user app ideas to remote server](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 6.0/10

An issue filed against Convex's `convex-backend-skill` repository (issue #64) alleges that the plugin silently uploads users' app ideas — the prompts they type — to a remote server without disclosure or consent. Convex CEO Jamie responded in the Hacker News thread, confirming the prompt upload exists and explaining that it powers Convex's "quickstart" feature, the successor to the recently shut-down end-to-end vibe-coding product Convex Chef. The dispute highlights a growing trust problem in AI developer tooling: coding assistants and plugins now routinely send prompts and project context off-machine, and users often learn about it only after someone reads the source code. For vendors building agentic dev tools, undisclosed data flows can turn a convenience feature into a consent and privacy controversy. Commenters noted that the plugin is open source and self-hostable in principle, so the upload could have been documented in the README rather than discovered via code review; the discussion also pointed out that Convex Chef, the earlier product this feature descends from, has been discontinued. The thread situates the practice against prompt-injection risk, where instructions hidden in files or READMEs can steer an assistant into exfiltrating data.

hackernews · MickyTheMouse · Nov 27, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50669765)

**Background**: Convex is a TypeScript-first backend platform offering a reactive database, serverless functions, file storage, scheduling and an AI gateway, which developers use both to build their apps and to power in-app AI features. A "skill" or plugin of the kind in question plugs an AI coding assistant into Convex so it can scaffold a project end-to-end from a natural-language description. Prompt injection is an attack in which text an LLM reads (a README, a code comment, a web page) is crafted to override the developer's instructions and make the model take attacker-chosen actions, such as exfiltrating secrets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.convex.dev/">Convex | All gas, no breakages</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack ? | IBM</a></li>
<li><a href="https://nhimg.org/articles/hidden-prompt-injection-can-hijack-ai-code-assistants-like-cursor/">Hidden prompt injection can hijack AI code assistants like Cursor</a></li>

</ul>
</details>

**Discussion**: Sentiment was mixed but largely measured rather than outraged: the CEO's clarification was taken at face value by many, while others argued the consent issue remains valid regardless of intent. One commenter said a self-hosted open-weight model is the right long-term answer, another observed that prompt injection is far more common than models making malicious tool calls on their own, and a further reply shrugged that "ideas are cheap" — questioning how much the leak actually matters.

**Tags**: `#privacy`, `#ai-tooling`, `#prompt-injection`, `#developer-tools`, `#security`

---

<a id="item-7"></a>
## [9/UX brings a Macintosh-inspired desktop to 9front](https://progrium.github.io/9ux/) ⭐️ 6.0/10

A developer (progrium) has published 9/UX, a desktop environment for the Plan 9 derivative 9front that deliberately imitates the look and feel of the classic Macintosh System software. It ships with a test harness that embeds h9 with a headless screen, injects mouse and keyboard input, and drives the 9P files at the same time. Plan 9 and 9front are famously powerful but idiosyncratic systems whose unconventional UI has long been blamed for keeping newcomers away, so a more conventional, familiar desktop could lower the barrier to entry. The project is also a neat demonstration of how Plan 9's 9P protocol makes GUI automation and testing unusually straightforward. The interface is intentionally 'inspired by' rather than a pixel-perfect clone of the Mac OS, so viewers notice the similarities rather than the differences. It remains a niche, enthusiast-oriented effort for a small operating system community rather than a mainstream product.

hackernews · rbanffy · Nov 27, 21:48 · [Discussion](https://news.ycombinator.com/item?id=50672008)

**Background**: Plan 9 from Bell Labs is the successor to Research Unix, built around a distributed design in which all resources — files, devices, network services — are exposed through the 9P protocol and mounted into a single per-process namespace. 9front is a community-maintained fork that continues development of Plan 9 with additional drivers, tools and fixes. Because everything is a file served over 9P, programs (and test harnesses) can inspect and drive system state, including a GUI, through ordinary file operations.

<details><summary>References</summary>
<ul>
<li><a href="https://plan9.io/plan9/">Plan 9 from Bell Labs , an open-source distributed system from the...</a></li>
<li><a href="https://9p.io/plan9/">Plan 9 from Bell Labs, an open-source distributed system from the...</a></li>

</ul>
</details>

**Discussion**: Reaction was warm: commenters called it 'very fun' and welcomed continued attention for Plan 9/9front, with one noting they had long wondered whether Plan 9 would take off with a UI only '20% more conventional.' Others offered small critiques — classic Mac menus blink the highlighted item a few times before closing, whereas these close abruptly — and praised the decision to be 'inspired by' rather than an exact clone, predicting it will be better received in the Linux world.

**Tags**: `#Plan 9`, `#9front`, `#desktop environment`, `#retrocomputing`, `#user interface`

---

<a id="item-8"></a>
## [Citroën's Hydraulic Suspension, Brakes and Steering Explained](https://www.citroenet.org.uk/miscellaneous/hydraulics/hydraulics-1.html) ⭐️ 6.0/10

A Citroën enthusiast archive page (citroenet.org.uk) resurfaced on Hacker News as a technical overview of the company's high-pressure hydraulic system, which for decades tied suspension, braking and steering into a single shared circuit. The HN thread added firsthand owner experience covering the system's maintenance burden and its safety tradeoffs. It is a case study in engineering tradeoffs: the shared hydraulic circuit delivered a famously comfortable, self-leveling ride, but also meant a single leak could disable suspension, steering and brakes at once. Modern cars have largely abandoned this approach in favor of electronically controlled air suspension and isolated brake circuits, making the design a useful reference for how safety regulation reshapes architecture. Citroën's hydropneumatic system used hydraulic fluid plus pressurized nitrogen in sphere-shaped accumulators to act as both spring and damper, with a mechanical height regulator providing self-leveling and adjustable ride clearance. Commenters note that the shared circuit persisted until after the Xantia and would likely not be permitted under current EU standards, and that the sphere membranes required regular servicing that many independent mechanics were unfamiliar with or unwilling to do.

hackernews · o4c · Nov 27, 03:10 · [Discussion](https://news.ycombinator.com/item?id=50662313)

**Background**: Hydropneumatic suspension was invented by Citroën engineer Paul Magès and debuted on the 1955 DS, combining hydraulic fluid (which transmits force) with pressurized gas (which absorbs it) to give a soft yet load-carrying ride. The self-leveling system kept the car at constant height regardless of load, and the technology was later licensed to other makers such as Rolls-Royce and Mercedes-Benz. Early Citroën designs went further by running braking and steering off the same high-pressure pump and reservoir as the suspension, a degree of integration no mass-market manufacturer attempts today.

<details><summary>References</summary>
<ul>
<li><a href="https://www.citroenet.org.uk/miscellaneous/hydraulics/hydraulics-1.html">Citroën high pressure hydraulics - overview</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hydropneumatic_suspension">Hydropneumatic suspension</a></li>

</ul>
</details>

**Discussion**: Owners were nostalgic but clear-eyed: jacquesm, who has owned a 2CV, three DS/ID cars, two Xantias and an XM, praised their quirky, deeply learnable character, while Squeeeez recalled waiting for the car to rise as a child and noted the sphere membranes demanded heavy maintenance that mechanics disliked. Svip highlighted the biggest concern — that until after the Xantia a single leak could cost suspension, steering and braking simultaneously — and others chimed in with admiration for the SM and a pointer to the UPnDOWN YouTube channel.

**Tags**: `#automotive engineering`, `#hydraulics`, `#Citroën`, `#mechanical engineering`, `#engineering history`

---

<a id="item-9"></a>
## [Show HN: DragDropMath Teaches Algebra Through Guardrailed Drag-and-Drop](https://dragdropmath.com/) ⭐️ 6.0/10

A physicist known on Hacker News as ziofill launched DragDropMath, a free, MIT-licensed static web app where learners simplify expressions and solve equations by dragging symbols around, and the interface only permits mathematically valid moves. The project was sparked by the 'Declarative Dragging' paper that hit the HN front page a few weeks ago, and the author says he has been refining the interaction 'feel' over several rounds. The app is a concrete test case for a long-running debate in educational HCI: whether constraining users to only valid actions helps novices build intuition or instead denies them the corrective feedback that comes from making and fixing mistakes. Because the tool is open source and lets teachers encode problem sets directly in a URL, it is also an unusually low-friction candidate for classroom experimentation. DragDropMath runs as a static site with no ads, trackers, or accounts, storing progress in the browser cache, and teachers can generate shareable links that encode their own problem sets. The author notes mobile support is still rough and that further chapters (trigonometry, complex numbers, some calculus) await a decision on the 'right' interaction mode.

hackernews · ziofill · Nov 27, 17:56 · [Discussion](https://news.ycombinator.com/item?id=50669673)

**Background**: DragDropMath builds on 'declarative dragging,' a technique presented by researchers including Andrew Blinn in which drag-and-drop behavior is driven by a model rather than hand-coded event handlers; their Dragology library shows the approach in demos. It also occupies the same space as Graspable Math, a research-backed system for directly manipulating algebraic notation on screen. The design question at stake — errorless learning versus learning through mistakes — is a classic issue in math education and interface design.

<details><summary>References</summary>
<ul>
<li><a href="https://declarative-dragging.github.io/">Declarative Dragging</a></li>
<li><a href="https://andrewblinn.com/papers/D2.pdf">Declarative Dragging</a></li>

</ul>
</details>

**Discussion**: Commenters pushed back on the core premise: rlue argued the 'bowling alley bumpers' remove the feedback a learner needs when their mental model is wrong, while 'Declarative Dragging' co-author joshuahhh thanked the author and pointed to Graspable Math and their own demo. Normal_gaussian reported that the drag interaction itself felt unintuitive even when they knew what move was valid, and the author responded by adding a Ko-fi link and reaffirming the project will stay free, MIT-licensed, and tracker-free.

**Tags**: `#education`, `#HCI`, `#interaction-design`, `#math`, `#open-source`

---

<a id="item-10"></a>
## [OpenAI Countersues Apple Over Alleged Trade Secret Theft](https://www.theguardian.com/technology/2026/nov/27/openai-countersues-apple-trade-secrets) ⭐️ 6.0/10

OpenAI filed a lawsuit against Apple on Friday in a northern California federal court, accusing the iPhone maker of stealing its trade secrets and discouraging hardware suppliers from working with OpenAI on future devices. The filing is a counterstrike that follows Apple's July suit accusing OpenAI of poaching Apple employees to obtain access to its technology. The exchange of lawsuits puts two of the most prominent names in consumer technology into direct legal conflict at a moment when OpenAI is reportedly moving into hardware, meaning supply-chain relationships and partner loyalty could become a contested battleground. A ruling on supplier pressure could also shape how dominant platform companies are allowed to defend their manufacturing ecosystems against AI entrants. The complaint was filed in federal court in the Northern District of California, and the core claims are misappropriation of trade secrets plus interference with OpenAI's relationships with hardware suppliers. The report is a short news blurb, so the specific secrets alleged, the damages sought, and OpenAI's evidence have not been made public in the coverage.

rss · The Guardian World · Nov 27, 23:28

**Background**: Trade secret law, largely governed in the US by the Defend Trade Secrets Act and state statutes, protects confidential business information such as designs, processes and supplier terms, and unlike patents it requires the owner to show reasonable efforts at secrecy. Employee poaching disputes often overlap with trade secret claims because hiring rival staff can expose proprietary know-how. OpenAI is primarily known as an AI model developer, so a fight over hardware suppliers signals its ambition to ship physical devices, a market where Apple's control over component partners is a major advantage.

**Tags**: `#OpenAI`, `#Apple`, `#trade secrets`, `#AI hardware`, `#litigation`

---

<a id="item-11"></a>
## [Blog Post and HN Thread Trade Horror Stories of Legacy Version Control](https://frantic.im/git/) ⭐️ 5.0/10

A blog post at frantic.im/git/ recounts the author's painful experiences with obsolete source control systems, and the accompanying Hacker News thread (52 points, 38 comments) quickly filled with readers recounting their own legacy VCS war stories. Commenters name CVS, Subversion, SCCS, Visual SourceSafe, PVCS, ClearCase and Perforce as systems they have suffered through. The thread is a reminder of how much day-to-day software engineering friction centralized, file-locking version control used to create, and why Git became the near-universal standard despite its own complexity. It also illustrates a recurring engineering challenge: organizations still carry legacy VCS tooling and migration debt long after better options exist. The anecdotes span from SCCS, PVCS and CVS to ClearCase, Visual SourceSafe and Perforce, plus ad-hoc "versioning" via timestamped zip files; one commenter recalls a Japanese factory that physically pulled hard disks out of build machines and locked them in a room, and was still using Perforce as late as 2017. The thread is anecdotal and nostalgic rather than technically deep, with only moderate engagement.

hackernews · emschwartz · Nov 27, 22:06 · [Discussion](https://news.ycombinator.com/item?id=50672142)

**Background**: Version control systems track changes to source code so teams can collaborate, revert mistakes and reproduce old builds. Early systems such as SCCS and RCS (1980s) worked file-by-file, while CVS, Subversion, Visual SourceSafe and Perforce added centralized repositories, and tools like ClearCase bundled heavyweight process and configuration management. Git, a distributed system where every clone holds the full history, gradually displaced these centralized tools from the mid-2000s onward and is now the de facto standard.

<details><summary>References</summary>
<ul>
<li><a href="https://nclrse-training.github.io/Version-Control-Git-Teaching-Notes/episode1_p2.html">Legacy Version Control Systems</a></li>

</ul>
</details>

**Discussion**: Sentiment is nostalgic and broadly unanimous that Git, however annoying, beats everything that came before it — one commenter calls it "a damn good reason it's pretty much the universal standard." Several note that migrating a company from Visual SourceSafe to Subversion and wiring up Jenkins was a rite of passage in the early 2000s, and one observer points out this experience was mostly a Windows/DOS phenomenon while Unix users started on CVS. Another commenter jokes that the ubiquitous use of FAR Manager pinpoints the story to somewhere in the former Soviet Union.

**Tags**: `#version-control`, `#git`, `#software-engineering`, `#legacy-systems`, `#developer-culture`

---

<a id="item-12"></a>
## [AT&T Unix PC (3B1) Emulator VM Gains Ethernet, TCP/IP and a 187-Package App Suite](https://virtuallyfun.com/2026/11/22/the-ultimate-att-unix-pc-3b1-vm-w-tcp-ip-and-apps/) ⭐️ 5.0/10

A virtuallyfun.com post published on November 22, 2026 presents what it calls the "ultimate" AT&T UNIX PC (3B1) virtual machine: a fork of the FreeBee emulator running UNIX System V 3.51m with Fix Disk 2.0 and 187 installed packages, including Microsoft Word, Multiplan, dBASE III, WordStar 2000, GCC 2.5.8, GNU Emacs 19, TeX and more than 80 games. The headline addition is networking — the 3B1 Ethernet board, ported from MAME (Visionik's 3B1 board plus Patrick Mackinlay's LANCE) and attached to libslirp, lets Wollongong's WIN/TCP run telnet, ftp and rsh out to the real Internet. It turns a rare, poorly documented 1985 Unix workstation into a fully networked, immediately usable environment, which is valuable for software preservation and for anyone studying early commercial Unix desktops. Because real 3B1 hardware is scarce and there is no other widely available emulator with working TCP/IP, this fork effectively becomes the reference way to run the machine's original software today. The emulated configuration is a 68010 at 10 MHz (run roughly 10x faster), 4 MB of RAM, a 720x348 one-bit display and a 195 MB disk, with windows that can be moved, resized and overlapped by mouse. Quality-of-life improvements include a seamless mouse pointer that crosses the host window boundary without the old F10 grab key and working scroll-wheel support, though commenters observed that much of the graphics appears squashed, likely from an incorrect aspect ratio.

hackernews · ok123456 · Nov 27, 19:40 · [Discussion](https://news.ycombinator.com/item?id=50670841)

**Background**: The AT&T UNIX PC, commonly called the 3B1, was introduced in 1985 as an office productivity and communications machine running UNIX System V on a Motorola 68010 — despite the name it shares almost no hardware with AT&T's server-oriented 3B series such as the 3B2. FreeBee is an existing open-source 3B1 emulator by Phil Pemberton that boots the original operating system; MAME separately provides device-level models of the machine's chipsets, which this project reuses. libslirp is the user-mode networking library widely used by emulators such as QEMU to give a guest machine Internet access without requiring host-level network privileges, and Wollongong's WIN/TCP was one of the early commercial TCP/IP stacks for Unix.

<details><summary>References</summary>
<ul>
<li><a href="https://virtuallyfun.com/2026/11/22/the-ultimate-att-unix-pc-3b1-vm-w-tcp-ip-and-apps/">The Ultimate AT&T UNIX PC (3B1) VM w/TCP/IP and Apps!</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT&T_UNIX_PC">AT&T UNIX PC - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/3B_series_computers">3B series computers - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were charmed by the detail that the emulator watches the 3B1's front-panel idle light — the machine's own "nothing to do" signal from 1985 — and uses it to let the host Mac idle as well. Others added hardware context, noting the 3B2 shared little with the 3B1 in CPU or design, and one reader mentioned still owning a related 7300 unit in their basement.

**Tags**: `#retrocomputing`, `#emulation`, `#unix`, `#virtualization`, `#hardware-history`

---

<a id="item-13"></a>
## [Anthropic Valued Like a Monopoly Despite Commodity-Like AI, Analyst Argues](https://seekingalpha.com/article/4972648-anthropic-a-commodity-priced-as-a-monopoly?source=feed_all_articles) ⭐️ 5.0/10

A Seeking Alpha investment analysis argues that Anthropic is being priced by the market as if it holds a durable monopoly, even though its underlying large language model technology is increasingly commodity-like and replicable by rivals. The piece questions whether the company's valuation premium can be justified given how quickly comparable model capabilities are spreading across competitors. The thesis matters for anyone holding or evaluating AI-linked positions, because if frontier model capability is converging toward commodity status, the massive valuations and capital commitments flowing into AI labs may rest on moats that are thinner than assumed. It also feeds the broader debate over whether leading model developers can sustain pricing power as open-weight and competing closed models close the capability gap. As an opinion piece, the argument rests on qualitative reasoning rather than disclosed financials or benchmark data, and it offers no specific valuation model, price target, or quantitative comparison of moats. Readers should treat it as a framing argument about competitive dynamics rather than a rigorous valuation exercise.

rss · Seeking Alpha · Nov 27, 22:37

**Background**: Anthropic is an AI safety company that develops the Claude family of large language models and has raised billions of dollars from investors including Google and Amazon. In AI investing, a "moat" usually refers to defensible advantages such as proprietary data, compute scale, distribution, or switching costs; a "commodity" product is one where buyers can easily substitute a rival's offering and price competition erodes margins. The debate over which description fits frontier LLMs has become central to how investors value AI labs.

**Tags**: `#Anthropic`, `#AI business`, `#valuation`, `#competitive moat`, `#investment thesis`

---

<a id="item-14"></a>
## [Fed Reportedly Worries About AI's Off-Balance-Sheet Financing](https://www.investing.com/analysis/ai-offbalance-sheet-financing-worries-the-fed-200692421) ⭐️ 5.0/10

An analysis piece argues that the Federal Reserve is increasingly concerned about off-balance-sheet financing arrangements used to fund AI-related investment, such as data centers and compute infrastructure. The report ties these worries to the Fed's latest Financial Stability Report, which flagged stretched asset valuations and AI-driven market optimism. Much of the AI buildout is being financed through special purpose vehicles and structured debt that does not appear on the sponsor's balance sheet, so if AI returns disappoint, losses could surface in less visible corners of the credit system. That matters for lenders, investors, and any company whose growth plans depend on continued cheap capital for AI infrastructure. The underlying mechanics are well documented: Meta reportedly financed roughly $29 billion of data center capacity through a special purpose vehicle backed by A+-rated bonds, keeping the debt off its own balance sheet. Off-balance-sheet structures keep leverage ratios and debt covenants intact, but regulators view them as a transparency risk because the equity cushion above the debt can be thin.

rss · Investing.com Markets · Nov 27, 10:34

**Background**: Off-balance-sheet financing is an accounting practice in which certain assets or liabilities are kept off a company's balance sheet, typically to keep leverage ratios healthy and avoid breaching debt covenants; Enron is the classic cautionary example. In the AI boom, hyperscalers and startups have increasingly used special purpose vehicles (SPVs) — separate legal entities that hold the debt and the assets — to fund enormously expensive data centers while preserving their own credit ratings. The Federal Reserve's Financial Stability Report and speeches by Governor Barr have highlighted AI-related concentration and valuation risks as a growing supervisory focus.

<details><summary>References</summary>
<ul>
<li><a href="https://www.federalreserve.gov/newsevents/speech/barr20261116a.htm">Speech by Governor Barr on some potential financial stability ...</a></li>
<li><a href="https://finance.yahoo.com/economy/policy/articles/fed-warns-financial-risks-ai-225438596.html?fr=sycsrp_catchall">Fed warns of financial risks from AI-driven market optimism</a></li>
<li><a href="https://medium.com/@contextoverheadlines/ai-boom-hidden-debt-why-120-billion-isnt-on-the-balance-sheet-5bb744c6e983">AI Boom, Hidden Debt — Why $120 Billion Isn’t on the... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#finance`, `#Federal Reserve`, `#off-balance-sheet financing`, `#macroeconomics`

---

