[Water

& Music](/)

* [Data](/data)
* [Event Recaps](/event-recaps)
* [Archive](/archive)
* [Services](/services)
* [Membership](/membership)

* [Data](/data)
* [Event Recaps](/event-recaps)
* [Archive](/archive)
* [Services](/services)
* [Membership](/membership)

---

![](https://imagedelivery.net/jAAhyfIbmIkTmPTuFjiUtw/05a0f990-22b5-4b08-4bb1-ec9d37e44b00/xlg)

# How music AI attribution actually works

By:Cherie HuAlexander FloresYung Spielburg

Published:2025-04-07

The state of music AI today can be measured in the millions — millions
of dollars
[raised](https://www.waterandmusic.com/music-tech-money-flows-2024), millions of users
[engaged](https://www.waterandmusic.com/the-new-music-ai-stack-nyc-takeaways), millions of AI-generated tracks
[uploaded](https://newsroom-deezer.com/2025/01/deezer-deploys-cutting-edge-ai-detection-tool-for-music-streaming/) to streaming services.

As the market continues to grow at breathtaking speed, an urgent
business question has emerged:
**Who deserves credit and compensation when AI generates music?**The answer could determine how billions in potential revenue
flow through the music economy in the coming years.

## **Introducing attribution**

**Attribution** — or the linking of AI outputs back to
the specific training inputs that influenced them — underpins the
ideal of a more granular rights holder compensation framework for AI.

Unlike copyright or deepfake detection systems that simply flag
similarity or infringement, attribution aims to establish
*causal* relationships between inputs and outputs. The concept
overlaps with the fields of
**[interpretability](https://www.splunk.com/en_us/blog/learn/explainability-vs-interpretability.html)** **[and](https://www.splunk.com/en_us/blog/learn/explainability-vs-interpretability.html)** **[explainability (XAI)](https://www.splunk.com/en_us/blog/learn/explainability-vs-interpretability.html)**, which seek to understand how a model produces output for a given
input.

For the music industry, attribution tech can help answer questions
like:

* Which songs in the training data **most influenced** this output?
* **How strong** was each influence, and how should we
  quantify it?
* What **specific musical elements** were borrowed or
  transformed?

Several startups are tackling this complex problem with their own
distinct approaches.
**[Musical AI](https://www.wearemusical.ai/)**, **[Sureel](https://sureel.ai/)**, and **[Soundverse](https://www.soundverse.ai/)** promise more granular, model-level tracking of influence, while
others like **[LANDR](https://www.landr.com/fairai/)**, **[Source Audio](https://www.sourceaudio.com/)**, and **[Lemonaide](https://www.lemonaide.ai/)** offer simpler, pro-rata splits based on total dataset contributions.
These ventures are also actively brokering a new generation of AI
licensing deals between developers and rights holders, helping shape
industry standards ahead of regulation.

In the sections ahead, we'll examine some of the technical
underpinnings of attribution, the commercial frameworks being built
around them, and the challenges in deploying these tools at scale.
More than a mere technical curiosity, attribution will likely
determine how — and for whom — the music industry thrives in an
AI-centric future.

---

## **Watch our webinar**

For a video walkthrough of attribution with visual references, we recommend watching the following recording of a webinar we presented to Water & Music members. Links to nearly all the papers we reference in the webinar are included throughout this written report.

---

## **But wait… what are we attributing?**

**While many compare music AI generation to sampling, the two processes
operate fundamentally differently.**

Traditional sampling takes identifiable fragments from existing
recordings; think, for instance, of the
[iconic drum break](https://www.youtube.com/watch?v=jOCNmimkFTs&ab_channel=ArmandoDrumBreaks) from "Funky Drummer" appearing in hundreds of hip-hop tracks. In
contrast, AI models
**absorb musical concepts at a more abstract level**,
learning patterns and concepts rather than merely copying
sections. These learned patterns are captured across its
[multilayered architecture](https://x.com/brandon_xyzw/status/1824245241769033894), forming an intricate weave of dependencies — similar to a
[modular synth](https://youtu.be/lJROZv3y270?si=zhqubuMRdmP05fu4), where each module represents its own layers with many parameters to
tweak, each change cascading a complex network of changes. A single
AI-generated track will draw from dozens of abstract layers of influence,
which are challenging to map computationally and with 100% confidence.

### **Sonic characteristics**

When examining any AI-generated song, multiple dimensions of musical
influence come into play simultaneously:

* **Composition.** AI models learn fundamental musical
  structures like chord progressions, melodic patterns, and longer song
  forms. A model might learn the distinctive I-V-vi-IV progression that
  powered countless pop hits, without attributing it to a specific
  creator. This raises a critical question: When an AI recreates a common
  chord sequence, who (if anyone) deserves attribution?
* **Recording.** AI models also absorb production techniques,
  sonic textures, and mixing approaches from the recordings they train on.
  For instance, models exposed to lo-fi hip-hop beats often internalize
  techniques like vinyl crackle textures, relaxed drum compression, and
  intentionally reduced high-frequency content.
* **Time.** Unlike static media like images, music unfolds
  over time in ways that compound complexity. The introduction of a song
  influences later sections, creating causal chains that attribution
  systems must somehow trace. Moreover, different moments in a single
  AI-generated song might draw from entirely different sources in the
  training data.

### **Beyond audio: The full attribution picture**

The attribution challenge extends far beyond audio files alone. A fully
comprehensive view would consider:

* **Data augmentation.** AI developers routinely expand their
  training datasets by creating modified versions of existing data — e.g.
  altering pitch, tempo, or adding background noise for a single song,
  which can generate thousands of derivatives. This process exponentially
  complicates attribution: If a model trains on 50 variations of one song,
  how should that impact credit allocation?
* **Prompt engineering.** Text-to-music generators like Suno
  and Udio rely on written descriptions from users that shape musical
  output. While the U.S. Copyright Office has
  [ruled](https://www.waterandmusic.com/music-ai-copyright-webinar-recap/) that prompts alone typically don't warrant copyright protection, they
  undeniably influence the creative result. Should exceptionally detailed
  prompts receive attribution alongside training data?
* **Multimodal influences.** Newer AI systems like Tencent’s
  [XMusic](https://arxiv.org/abs/2501.08809) can generate music
  to accompany video, learning cross-modal relationships between visual
  emotion and sound. When visual data directly influences musical
  decisions about timing, dynamics, and emotional tone, attribution
  frameworks should arguably account for this additional layer of
  complexity.
* **Model design.** Different AI
  architectures process musical data in different ways,
  meaning choices about model design can significantly influence which
  training inputs have the strongest impact on final outputs.

### **The stakes: Attribution as value distribution**

**Every attribution system ultimately makes value judgments about which
musical elements deserve compensation.**

These judgments have substantial financial implications:

* A system that overvalues melodic similarity might disproportionately
  compensate songwriters over producers.
* Attribution focused on recording characteristics might favor master
  rights holders over composers.
* Models that track thousands of minor influences could fragment payments
  into economically meaningless amounts.

These decisions are both technical and ethical in nature, and will set
precedents that could redefine music's economic structures for decades to
come.

---

## **How do we attribute?**

The gap between the music industry's ideal of attribution — a detailed
royalty sheet for every AI-generated song — and technical reality remains
substantial. Let's examine how some common attribution technologies
actually work, and why each approach comes with significant tradeoffs that
shape the commercial solutions emerging in the market.

### **Influence functions: The statistical ideal**

A fundamental concept in statistics, influence functions measure how much
a single data point affects a model's output, by comparing results with
and without that point included (“leave-one-out”). The principle is
straightforward:
**The more a prediction changes when a specific data point is removed,
the more influential that point is considered to be.**

As a practical example: Picture a music AI that generates a trap beat.
Influence functions would theoretically measure how different that beat
would be if Drake's "God's Plan" were removed from the training data,
versus removing Kendrick Lamar's "HUMBLE." Whichever removal causes a
greater change would be considered more influential to the output.

Despite their elegant simplicity,
[influence functions face several significant limitations](https://link.springer.com/article/10.1007/s10994-023-06495-7). First, they tend to
**overemphasize outliers in the data**, as unique examples
can disproportionately affect the output. More critically, a
"leave-one-out" approach becomes impractical with modern AI models: For a
model trained on millions of songs, computing true influence would require
retraining the model millions of times — a task that would take years even
on advanced hardware.

To address these computational challenges, the explainable AI field has
[developed approximation techniques](https://arxiv.org/pdf/2209.05364) that attempt to capture the spirit of influence functions without the
full computational burden. However, these approximations often break down
when applied to neural networks — i.e. the foundation of modern generative
AI. The result is that these approximated influence measurements no longer
reliably indicate how the model would actually behave if specific training
data were removed.

### **Embeddings: Similarity as a proxy**

Whether we’re talking about Google’s search results, a photos app grouping
images of your face, or Spotify’s song recommendations, a critical
component of modern AI is the ability to
**mathematically quantify similarity**. These similarity
mapping systems rely on **embeddings**: Translations of raw,
unstructured data (text, images, audio) into compact numerical coordinates
in an abstract space, where similarity can be measured precisely.

For example, a song’s raw audio waveform, typically chaotic and
computationally unwieldy, might be compressed via embedding into a vector
like [0.24, -0.73, 1.2, ..., 0.45], a string of hundreds or even thousands
of numbers. These vectors act as GPS coordinates in an abstract space —
but instead of two dimensions (latitude/longitude), they use hundreds to
capture nuanced relationships. In this space, proximity reflects perceived
similarity: Two songs near each other might share tempo, mood, or genre
traits a human would recognize. Music projects like
[Everynoise](https://everynoise.com/) are exemplary in how they
visualize similar genres as clusters in embedding space.

Crucially, however, **proximity implies resemblance,** **not** **causation**. While an AI-generated
track near Taylor Swift’s songs might directly sample her work, it might
also be echoing her style unintentionally, or coincidentally converging on
similar patterns. A clone of a song’s "coordinates" might be theft — or
pure algorithmic pareidolia.

For rights holders, this distinction is critical: Embeddings can flag
potential influences (*what* sounds alike), but cannot interrogate
the creative process (not *why* it sounds alike).

### **Watermarking: Digital receipts for data usage**

Watermarking takes a different approach entirely, embedding hidden signals
(e.g. inaudible tones, spectral tags, metadata) in training data that
survive the generation process and appear in outputs. Unlike the other
methods, watermarking doesn't try to measure degree of influence; it
simply confirms
**whether specific training data contributed to an output at all.**

This significantly limits watermarking’s scope in the context of music
rights. For example, an AI trained on a watermarked pop song might learn
its "catchy hook" structure but generate an original melody, leaving the
watermark intact yet revealing nothing about this creative borrowing.

As we’ve
[covered previously](https://www.waterandmusic.com/music-ai-content-copyright-detection-deepfakes), watermarking is also incredibly vulnerable to inaccuracy and
manipulation. While detecting watermarks in AI outputs can confirm the
tagged data was part of the training set, they often degrade during
training or generation, leading to false negatives. In response,
researchers have adopted convoluted workarounds, like
[applying the same signal to massive portions of a dataset](https://arxiv.org/pdf/2412.08549). Imagine tagging every item in a warehouse with the same barcode; this
brute-force approach might prove the dataset was used, but it’s useless
for identifying specific tracks that influenced the output.

Adversaries can also exploit loopholes such as stripping watermarks via
audio editing (e.g., EQ filtering), or training models on "clean,"
unmarked copies of the same content. In short, watermarking answers a
limited question — and even then, not reliably.

### **Challenges in the details**

Even the most sophisticated attribution technologies face inherent
challenges rooted in how modern AI systems work:

* **Architectural complexity.** As detailed in the previous
  section, today's music AI systems transform raw inputs into songs
  through nonlinear conceptual stages, blending influences from thousands
  of training examples into fundamentally new outputs. Current attribution
  tools cannot reliably map how specific artists’ works contribute to
  these intermediate transformations, particularly when examining
  subsystems that operate at different abstraction levels. This
  practically means there is a long tail of music data, all responsible
  for the model learning the fundamental concepts for “what is music,”
  that might not be credited.
* **Hidden dependencies.** AI systems often integrate
  specialized subsystems trained for distinct tasks, including components
  designed to process music in highly specific ways. For instance, some
  models employ preprocessing modules that compress musical data into
  streamlined representations (e.g. a latent space), optimizing
  computational efficiency during generation. These subsystems require
  their own training data; a compression module, for example, might be
  trained on vast datasets of raw audio to learn how to distill music into
  a compact, analyzable format. Though invisible to end users, this
  foundational preprocessing step shapes every output the system produces.
  This raises a critical question of whether data used to train such
  subsystems should be assigned a different value than data used in later
  stages of the pipeline.
* **Data debt and negative influence.** AI models don’t
  discern from the data they are fed; they learn as much from negative
  (i.e. low-quality or conflicting) examples as positive ones. How do we
  credit artists if their work inadvertently undermines another’s creative
  intent? Further complicating accountability,
  [recent research](https://arxiv.org/abs/2408.16333) shows
  isolating these negative influences may actually help improve models.
  For instance, a poorly mixed track might teach a system what to avoid,
  paradoxically making it more influential on the final result by showing
  what not to do.
* **Synthetic data.** As companies increasingly use
  [AI-generated data](https://www.waterandmusic.com/three-music-ai-trends-to-watch-in-2025-recording-takeaways) to train other AI models, attribution becomes a chain-of-custody
  problem. Each generation further obscures the original human sources,
  creating attribution chains that become increasingly difficult to trace.

These inherent constraints underscore why major players now face a dual
mandate: Refining imperfect tools while inventing entirely new commercial
frameworks to meet industry demands. The next section will examine
**how these players are building businesses despite — or perhaps because
of — the technical constraints in front of them.**

---

## **Who are the key players?**

While the technical challenges of attribution remain substantial, several
pioneering companies are developing commercial solutions that balance
future ideals with current market realities. Their diverse approaches
reveal not just different technical strategies, but fundamentally
different visions for how the music AI economy should function.

### **Sureel**

Founded by AI and robotics PhD Tamay Aykut,
**[Sureel](https://sureel.ai/)** has emerged as one of the most technically sophisticated players in
music AI attribution. They've secured
[multiple patents](https://patentimages.storage.googleapis.com/f9/5e/93/2256009606c620/US12013891.pdf) for their tech, and have inked partnerships with
[OpenPlay](https://www.kxan.com/business/press-releases/ein-presswire/765933251/openplay-signs-agreement-with-sureel-ai/) and
[Rostrum Pacific](https://www.musicbusinessworldwide.com/rostrum-pacific-unveils-ai-powered-music-distribution-platform-spaceheater/), (parent company of Rostrum Records), nearing 10 million registered assets under their belt.

Their key innovation is addressing what many consider the central problem
in music rights:
**Distinguishing between compositional and recording
contributions**.

Most attribution systems treat music as a single asset, and therefore only
examine recording-level similarities between outputs and training data,
without capturing compositional relationships. The discrepancy occurs
because training data often takes the form of recordings, as opposed to
separated recording and respective compositional (e.g. MIDI)
representations.

In practice, this can lead to a severe gap in financial outcomes between
both sides. For instance, when an AI generates a track with the same
melody as a training example, but with completely different
instrumentation and production, many attribution systems would miss this
connection entirely — potentially leaving songwriters unpaid while only
compensating the master rights holders.

Sureel's technology attempts to separate influences on melodies and lyrics
(publishing rights) from influences on production and performance (master
rights), with the ambition to go even more granular in the future to the
level of crediting specific performers of an original song. Their tech is
designed to be integrated during model training, with one of their
[patents](https://patentimages.storage.googleapis.com/f9/5e/93/2256009606c620/US12013891.pdf) outlining a process to track how individual pieces of data influence the
neural network throughout the training process.

### **Musical AI**

Co-founded by Sean Power, Nicolas Gonzalez Thomas, and Matt Adell (former
CEO of Beatport),
**[Musical AI](https://www.wearemusical.ai/)** is taking a similar infrastructure-focused approach to Sureel, building
attribution tech that can be integrated into other companies' AI
platforms.

The company is also actively brokering the rightsholder and developer
deals needed for their solution to scale. They have partnerships with the
music AI generator [Beatoven](https://www.beatoven.ai/) and
distributors
[Symphonic](https://www.billboard.com/pro/symphonic-musical-ai-training-partnership/) and
[Kanjian](https://www.musicbusinessworldwide.com/musical-ai-teams-up-with-chinas-kanjian-to-deliver-licensed-music-to-ai-developers/), and announced a
[CA$2.1M (~US$1.5M) funding round](https://www.digitalmusicnews.com/2025/02/06/genai-music-rights-musical-ai-funding/) in February 2025.

While specific technical details remain limited, a 2024 demo reviewed by
the W&M team showed their technology producing "royalty sheets" that
identify specific pieces of IP and their percentage influence on generated
outputs. Like other leading solutions, their system must be present from
the start of model training to be fully effective.

Due to the complexity of music rights, Musical AI’s current strategy is to
limit their IP partners to
**“one-stop rights holders” — i.e. those who own both their masters and
publishing**. This presumably narrows down their serviceable market to production
libraries like Epidemic Sound and Artlist that own all the rights to their
catalogs, or to DIY artists with no label or publisher signings.

Under the Musical AI x Beatoven deal, 30% of revenue from Beatoven’s
upcoming generative models will be distributed back to the artists and
rights holders who provided training data (aligning with collecting
society [GEMA](https://gema.de/)’s recommendations).

### **Soundverse**

**[Soundverse](https://www.soundverse.ai/)** — founded by Sourabh Pateriya (who previously co-invented Spotify’s
audio-to-MIDI converter
[Basic Pitch](https://basicpitch.spotify.com/)) — offers a
suite of AI tools geared towards content creators and hobbyist musicians,
including stem separation, lyric generation, text-to-audio synthesis, and
full track creation. Linnea Sundberg, Head of Operations at UnitedMasters
and former business exec at Splice and Spotify,
[joined](https://www.soundverse.ai/blog/article/linnea-sundberg-spotify-splice-joins-soundverse-ai-as-an-advisor) Soundverse as an advisor in February 2024.

In May 2024, Soundverse launched its
[Content Partner Program](https://www.soundverse.ai/partner),
which allows artists and rights holders to submit their content for
inclusion in training the company’s own AI models, in exchange for
receiving royalty payouts based on how their data is used.

Under this program, Soundverse has evolved its attribution approach
significantly through trial and error. They initially analyzed outputs for
similarity across multiple dimensions (voice similarity, song structure,
lyrics, instrumentation, key), but found this approach difficult to
implement reliably.

Their breakthrough came with integrating attribution directly into their
own foundational model. "**Attribution accuracy is very much dependent on the architecture, and
it's highest when it's infused with the model itself,**” Pateriya told us.

Now, rather than examining outputs after generation, Soundverse now tracks
how tokens flow through the model during training and generation. This
allows them to monitor which parts of the neural network are activated by
specific training examples, and therefore create a more accurate
connection between training inputs and generated outputs. The company is
still exploring exactly where in the model pipeline to implement
attribution — e.g. tracking token flow end-to-end versus focusing only on
final token generation.

On the other side, rights holders can access a partner portal to monitor
how their data influences generated content, with attribution mapped to
specific royalty payments.

Notably, Soundverse is one of the few companies today
**combining attribution tech with their own consumer-facing AI music
platform**. This vertical integration gives them a significant advantage: They can
tune their attribution system specifically for their own models, rather
than feel pressured to build a one-size-fits-all solution.

### **Simplified attribution alternatives**

Not all companies are pursuing technical attribution at the individual
song level. Several are opting for less tech-dependent deals with rights
holders, through simpler revenue-sharing and pro-rata payout models.

#### **Lemonaide**

Founded by Michael “MJ” Jacobs and Anirudh Mani,
**[Lemonaide](https://www.lemonaide.ai/)** launched in 2021 as a browser-based MIDI generator, and has since
expanded its product line to include
[Spawn](https://www.lemonaide.ai/spawn) (DAW plugin for MIDI
generation) and
[Collab Club](https://www.lemonaide.ai/collab-club) (producer-branded AI melody generator, partnering with the likes of
[Kato on the Track](https://www.lemonaide.ai/kato) and
[KXVI](https://www.lemonaide.ai/kxvi)).

With Lemonaide’s Collab Club models, attribution is straightforward: Each
AI model is trained exclusively on a single producer's data, with 100% of
attribution flowing back to that producer. Users agree to share 5% of
revenue with the producer for tracks exceeding one million streams.

Recognizing this single-source approach won't scale to larger datasets,
Lemonaide is developing what they call "**cohort-based attribution**," which categorizes outputs by genres and sub-genres (ranging from
hip-hop to Nepalese folk music), determines which cohort most influenced a
given output, and distributes revenue to all rightsholders who contributed
to that cohort. Importantly, this attribution still relies on detecting
output similarity — probabilistically attributing an output back to an
input cohort, rather than gaining insight into the internal mechanisms of
the models themselves.

“The idea isn’t to enforce traditional genre definitions, but rather to
create meaningful ‘groupings’ that help us trace influence in a way that
aligns with musical patterns, musical intention, and other production
related factors,” Mani told us over email. “Genres and subgenres are also
a great starting point because artists and rights-holders still think in
genre terms when using tools like ours. I anticipate we’ll move towards
more meaningful groupings organically as we keep working and improving.”

While Lemonaide is investing in more granular "fractional attribution" for
the future, they are prioritizing building trust with rights holders over
achieving near-term technical perfection. As Mani told us:
**"Attribution is as much a business, ethics, and trust problem as it is
a technical problem.”** In other words, a technically sound attribution system is worthless if
industry rightsholders won't adopt it.

#### **LANDR**

One of the earliest AI-native music tech companies,
**[LANDR](https://www.landr.com/)** has evolved from an automated mastering tool to a full-service platform
with distribution, sample libraries, and plugins. With over 6 million
registered users and tens of millions of mastered tracks, they have
substantial built-in market reach for their current and future AI tools.

Their
**[Fair Trade AI](https://www.landr.com/fairai/)** program allows artists who distribute through LANDR to opt into
providing their music as training data. Rather than attempting granular
attribution, LANDR will distribute 20% of revenue from AI products back to
contributing artists on a pro-rata basis, determined by the volume of
songs contributed to the dataset.

This approach sidesteps the technical challenges of precise influence
tracking, providing rights holders with a much more predictable revenue
model. The simplicity of this system may appeal to many independent
artists who value upfront transparency and predictability over potentially
higher but less certain returns from more complex attribution systems.

#### **Source Audio**

Music catalog management and sync licensing platform **[Source Audio](https://www.sourceaudio.com/)** is expanding into AI tools with their new platform
**[SongLab](https://songlab.ai/)**, which officially launched in February 2025. Their substantial dataset
includes 33 million tracks (14 million full mixes plus 19 million
alternate versions and stems), positioning them as one of the largest
rights-cleared music repositories available for AI development.

SongLab offers a comprehensive toolkit including lyric translation,
catalog augmentation (creating derivatives like remixes), stem separation,
and audio similarity search. Underlying these tools is a distinctive
approach to rights management that focuses on specificity rather than
flexibility of use.

Drew Silverstein, Head of AI Strategy at Source Audio, explained their
licensing framework over email: "Our agreements are limited to specific,
pre-defined use cases with strict guardrails preventing copying,
sub-licensing, or replacing human-created content with synthetic data. The
multi-year, fixed-term structure provides clarity and stability to all
parties rather than open-ended commercial exploitation."

Unlike systems that attribute ongoing royalties based on usage, Source
Audio's agreements build compensation directly into the upfront terms. "We
license access to data for training and improvement purposes within
carefully defined boundaries, which exclude the right to commercially
reproduce or distribute the original works," Silverstein noted. "The value
exchange is built into the upfront terms of the license, and additional
royalty mechanisms are not aligned with how the data is actually used."

#### **Human Native**

Founded by Jack Galilee and James Smith (formerly of Google's DeepMind),
**[Human Native AI](https://www.humannative.ai/)** is positioning itself as a broker of licensing deals between AI
developers and rights holders rather than a technology provider. The
company has won the
[Music Ally S:IX](https://musically.com/2024/11/07/and-the-winners-of-the-2024-music-ally-six-startups-contest-are/) startup competition, and is a member of the BPI’s latest
[Grow Music](https://musically.com/2024/10/01/bpi-picks-28-startups-for-its-grow-music-innovation-program/) innovation program.

Notably, Human Native has deliberately chosen not to pursue attribution
tech at all. Instead, they focus on facilitating dataset licensing deals
with fixed terms and upfront fees. Their marketplace model aims to
standardize these transactions, giving rights holders access to multiple
AI partners without negotiating individual deals with each. While they're
experimenting with revenue-sharing models, none depend on attribution to
individual pieces of content.

---

## **What does this mean for the music industry?**

After examining the sheer diversity of attribution and licensing
approaches in the music AI market, several critical insights emerge for
industry stakeholders:

### **Technical limitations shape deal structures**

The attribution deals being struck today directly reflect each company's
technical capabilities, rather than ideal market structures. Those without
granular attribution simply cannot offer usage-based royalty models
similar to traditional music licensing. Instead, they're creating
alternative compensation frameworks built around flat-fee licensing or
pro-rata data contribution volume.

These simpler approaches may appear less "fair" theoretically, but they
offer crucial advantages:

* **Predictability** — Rights holders can forecast revenue
  with greater confidence.
* **Transparency** — The terms are more easily understood by
  all parties.
* **Scalability** — These models don't require complex
  technical infrastructure.

### **The most critical infrastructure: Trust**

Several attribution companies are acting as deal brokers,
**suggesting that** **technical solutions alone don't solve the market coordination
problem.** This intermediary role is proving essential because:

* **Rights holders** need assurance about how their IP will
  be used.
* **AI developers** need confidence in the legitimacy of
  their training data.
* **Both sides** benefit from standardized deal terms and
  compliance verification.

Many of the attribution companies gaining early traction are those that
prioritize trust-building alongside technological development.

### **Strategic advantages for unified rights**

**Entities controlling both master and publishing rights** have substantial advantages in the AI training market. This explains why
early AI licensing deals are concentrated among:

* **Production music libraries** (e.g. Source Audio)
* **Digital distributors** with comprehensive rights (e.g.,
  Symphonic)
* **Artist-owned catalogs** (e.g. Soundverse)

These "one-stop shops" can move quickly without navigating complex
approval chains. For major labels and publishers with fragmented rights,
the path to AI monetization will likely require more sophisticated
attribution that can track and allocate revenue across multiple rights
holders.

## **Reframing the purpose of attribution**

The perhaps uncomfortable truth underpinning all of these findings is that
**perfect attribution for music AI doesn't currently exist.**

All the attribution approaches we studied provide approximations at best,
rather than definitive proof of influence. The options for rights holders
and AI developers today essentially boil down to:

1. Pursuing highly technical attribution methods that remain cumbersome to
   implement and audit, or
2. Adopting simpler solutions that compromise on detail, but offer more
   practical viability.

Ultimately, real progress hinges on confronting these limitations. Rights
holders must ask what "fair compensation" means in an environment where
every track contains countless micro-influences. Meanwhile, AI companies
must design systems transparent enough to build trust, while being candid
about where the tech still falls short.

At the same time, rather than viewing attribution as merely a technical
problem waiting to be solved, the industry might also benefit from
reconsidering its fundamental purpose.

Attribution itself isn’t even necessarily the end goal; rather, it's one
possible mechanism to
**ensure rightsholders are fairly compensated when their work contributes
to AI systems.**

Understanding this motivation helps explain why the companies featured in
this piece define attribution in such different ways. Some are building
fine-grained, forensic systems that aim to trace exactly what happened
inside a model. Others, limited by current tech, rely on approaches like
output analysis or similarity scoring — methods that echo traditional
musicology in infringement cases, but do not give primary source sight
into the models’ workings.

Interestingly, the best technology does not ensure "winning" in this
space; we already see companies able to gain trust and coordinate deals by
balancing commercial viability with practical constraints.

Hence, while there is a gap between what the market expects from
attribution and what the technology can actually deliver, if the goal is
compensating rights holders, then attribution is just one tool in the box,
and the right mix of incentives and innovation will eventually close that
gap.

The companies most likely to succeed won't necessarily be those with the
most technically sophisticated attribution systems, but rather those who
can solve the immense political challenge of fostering cross-industry
trust, and creating compensation frameworks that all parties view as both
practical and fair.

---

## Supplemental resources

[*Training data influence analysis and estimation: a survey*](https://link.springer.com/article/10.1007/s10994-023-06495-7)

[*Tracing Model Outputs to the Training Data*](https://www.anthropic.com/research/influence-functions)

[*Studying Large Language Model Generalization with Influence Functions*](https://www.youtube.com/watch?v=Q1h4NvveTZA)

[*Exploring Musical Roots: Applying Audio Embeddings to Empower Influence Attribution for a Generative Music Model*](https://arxiv.org/abs/2401.14542v1)

[*Is There A Coherent Theory of Attributing AI Training Data?*](https://michaelweinberg.org/blog/2024/07/15/ai-attribution-what-does-it-mean/)

[*MusicLIME: Explainable Multimodal Music Understanding*](https://www.semanticscholar.org/paper/MusicLIME%3A-Explainable-Multimodal-Music-Sotirou-Lyberatos/6ef47a7b18960a50d87abf3635f0e0302c424c5e)

[*AudioGenX: Explainability on Text-to-Audio Generative Models*](https://arxiv.org/abs/2502.00459v2)

[*Towards Assessing Data Replication in Music Generation with Music Similarity Metrics on Raw Audio*](https://arxiv.org/abs/2407.14364)

[*Mapping the Potential and Pitfalls of "Data Dividends" as a Means of Sharing the Profits of Artificial Intelligence*](https://arxiv.org/abs/1912.00757)

[*God Help Us, Let's Try To Understand AI Monosemanticity*](https://www.astralcodexten.com/p/god-help-us-lets-try-to-understand)

[*Watermarking Training Data of Music Generation Models*](https://arxiv.org/abs/2412.08549)

[*XAttnMark: Learning Robust Audio Watermarking with Cross-Attention*](https://arxiv.org/abs/2502.04230)

---

[MEMBER FAQ](/faq) [ARCHIVE](/archive) [SHOP](https://shop.waterandmusic.com/) [CONTACT](/contact)

© 2025 WATER & MUSIC. All rights reserved.
