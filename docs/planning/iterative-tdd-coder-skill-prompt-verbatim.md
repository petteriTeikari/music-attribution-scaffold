# Iterative TDD Coder Skill — Original Prompt (Verbatim)

> Saved verbatim on 2026-02-10. This is the user's original request that led to the design and implementation of the `self-learning-iterative-coder` skill.

---

Let's next create a iterative-tdd-coder Skill that knows how to write code as we did for academic writing here for .tex documents: /home/petteri/Dropbox/github-personal/sci-llm-writer/.claude/skills/iterated-llm-council using the self-correcting iterative approach popularized here https://www.theregister.com/2026/01/27/ralph_wiggum_claude_loops/ "Agentic AI
'Ralph Wiggum' loop prompts Claude to vibe-clone commercial software for $10 an hour
155 comment bubble on white
Developer behind it is sick with worry he might have changed software development in nasty ways
iconSimon Sharwood
Tue 27 Jan 2026 // 10:45 UTC
Feature Open source developer Geoff Huntley wrote a script that sometimes makes him nauseous. That's becaues it uses agentic AI and coding assistants to create high-quality software at such tiny cost, he worries it will upend his profession.

Here's the script :
while :; do cat PROMPT.md | claude-code ; done

Huntley describes the software as "a bash loop that feeds an AI's output (errors and all) back into itself until it dreams up the correct answer. It is brute force meets persistence." He calls the code and the technique it enables "Ralph," a homage to 1980s slang for vomiting, and to Simpsons character Ralph Wiggum and his combination of ignorance, persistence, and optimism.

The Register put it to Huntley that current human-in-the-loop practices mean developers use AI coding assistants as if playing table tennis: They send a prompt to produce some code over the net, and the LLM bats back some code. He accepted the metaphor, which assumes the developer/bot game continues until the human is satisfied the AI produced something useful, picks up the ball, and goes away to work.

Huntley's approach changes the game by telling a coding assistant to attempt to satisfy a developer's requests, assess whether it did so, then try again until it delivers the desired results. Humans remain in the loop, but enter the software development process later and less often than is the case today.

The developer has used his approach, and Anthropic's Claude Code service, to clone commercial products, a job it can achieve if provided with resources including source code, specs, and product documentation.

Huntley has documented how he used Ralph to create an a tax app for the ZX Spectrum, and later reverse-engineered and cloned an Atlassian product.

Huntley told us he used his techniques to clone a version of open source software a commercial vendor offers under a license he feels doesn't meet his needs. After accessing the company's source code and trans-piling it into another language, he used Ralph to drive Claude Code and create a clone. The results weren't great because he didn't have a spec for the product, but feeding the vendor's documentation into his loop meant Claude eventually produced better software.

The developer told The Register AI can tackle such tasks while consuming about US $10 of compute and/or SaaS resources each hour, a sum he points out is far closer to wages paid to fast food workers than the far better salaries earned by software developers.

Huntley even used his approach to develop a new programming language that he called "Cursed."

"It's cursed in its lexical structure, it's cursed in how it was built, it's cursed that this is possible, it's cursed in how cheap this was, and it's cursed through how many times I've sworn at Claude," he wrote.

What hath I wrought?
He also wonders if the fact it was possible to create Cursed might have hexed the software industry. Which is why Huntley's creation sometimes makes him feel nauseous, and why through 2025 he sometimes paused work on his ideas.

But he kept talking about them with other developers, and after a visit to Silicon Valley noticed considerable interest in his approach – especially among startups.

He says many participants in prominent startup incubator Y Combinator now use Ralph, and that the buzz their efforts created eventually saw Anthropic learn of his work and create a Ralph Wiggum Plugin for its Claude Code product. The creator of Claude Code, Boris Cherny, has said he uses Ralph.

Microsoft revokes MVP status of developer who tweeted complaint about request to promote SQL-on-Azure
Fancy some post-weekend reading? How's this for a potboiler: The source code for UK, Australia's coronavirus contact-tracing apps
Anthropic writes 23,000-word 'constitution' for Claude, suggests it may have feelings
Contagious Claude Code bug Anthropic ignored promptly spreads to Cowork
Huntley thinks he has stumbled upon an idea that can change software development, and perhaps entire industries.

Developers, he argues, should now spend more time thinking about writing loops that drive coding assistants to produce better output, rather than persisting with code reviews.

"Agile and standups doesn't make sense any more," Huntley said. "The days of being a Jira ticket monkey are over."

He also thinks that Ralph poses a profound challenge to any business. "Companies have a brand that can't be cloned and goodwill that can't be cloned," he told The Register. "But product features can now be cloned."

Huntley therefore expects that startups will use Ralph to clone existing businesses – especially SaaS outfits – and undercut the prices they charge because they can afford to do so using agentic coding that costs $10 an hour instead of having to pay a full staff of human coders.

And that's a scenario that could make many, many, people feel very sick indeed. ®" https://devinterrupted.substack.com/p/inventing-the-ralph-wiggum-loop-creator "Geoffrey Huntley argues that while software development as a profession is effectively dead, software engineering is more alive—and critical—than ever before. In this episode, the creator of the viral "Ralph" agent joins us to explain how simple bash loops and deterministic context allocation are fundamentally changing the unit economics of code. We dive deep into the mechanics of managing "context rot," avoiding "compaction," and why building your own "Gas Town" of autonomous agents is the only way to survive the coming rift.


1. Is 2026 the year of "Ralph Wiggum"?
If you have been on LinkedIn this week, you have seen Ralph Wiggum. But this isn't just a meme; it is a new paradigm for agentic coding. The "Ralph" technique is essentially a bash loop that feeds an AI's output (errors and all) back into itself until it dreams up the correct answer. It is brute force meets persistence. We are moving away from the idea of a single "genius" model toward a workflow where the loop is the hero, not the model. It might be inefficient, but for complex tasks, stubbornness is proving to be a quality all its own. Will you choo-choo-choose Ralph for your next project?

Read: Ralph Wiggum as a "software engineer"




2. Welcome to Gas Town
If "Ralph" is a single agent looping, "Gas Town" is an entire community of them. A new open-source orchestration system described by Steve Yegge, Gas Town manages scaling numbers of AI coding agents for parallel development. It is being described as "Kubernetes for agents." The core concept relies on the "Molecular Expression of Work" (MEOW), defining tasks in such granular steps that they can be picked up, executed, and handed off by ephemeral workers. Basically, a PRD under a microscope. We are entering the era of the agent assembly line, where code is limitless and coordination is the bottleneck.

Read: Welcome to Gas Town




3. Claude transcripts finally escape jail
Code tells you what happened; transcripts tell you how you got there. Simon Willison has released a new Python CLI tool that converts Claude Code transcripts into detailed, shareable HTML pages. This solves a major governance and workflow problem: auditability. Tools like this allow for "engineering reflection" away from the desk, reviewing an AI's reasoning logic while on a walk or at the gym.

Read: A new way to extract detailed transcripts from Claude Code


Simon Willison's Newsletter
A new way to extract detailed transcripts from Claude Code
In this newsletter…
Read more
a month ago · 71 likes · 6 comments · Simon Willison
4. The AI economic crisis hitting Open Source
The creators of Tailwind CSS have laid off most of their engineering team, citing a significant drop in documentation traffic and revenue. The issue came to light when a PR to add an /llms.txt file (to help AI scrape docs) was rejected by leadership. The logic is brutal but clear: AI consumes documentation to write boilerplate code, killing the traffic that drives revenue. Consider this a friendly reminder to support the open source projects you depend on.

Read: Tailwind CSS and the open source sustainability crisis




5. Developer productivity isn't a black box
Are you measuring your team against opaque formulas like DVI or DXI? Relying on subjective surveys (vibes) to gauge performance puts engineering leaders on the defensive and often hides the truth about what is actually dragging down delivery.

Our research shows that organizations with a balanced investment profile are 24% more likely to ship on time. Stop relying on black box consulting metrics that don't reveal what drives success. Get the data you need to align engineering with business strategy." https://ghuntley.com/loop/ "I've been thinking about how I build software is so very very different how I used to do it three years ago.

No, I'm not talking about acceleration through usage of AI but instead at a more fundamental level of approach, techniques and best practices.

Standard software practices is to build it vertically brick by brick - like Jenga but these days I approach everything as a loop. You see ralph isn't just about forwards (building autonomously) or reverse mode (clean rooming) it's also a mind set that these computers can be indeed programmed.


watch this video to learn the mindset

I'm there as an engineer just as I was in the brick by brick era but instead am programming the loop, automating my job function and removing the need to hire humans.

Everyone right now is going through their zany period - just like i did with forward mode and building software AFK on full auto - however I hope that folks will come back down from orbit and remember this from the original ralph post.

While I was in SFO, everyone seemed to be trying to crack on multi-agent, agent-to-agent communication and multiplexing. At this stage, it's not needed. Consider microservices and all the complexities that come with them. Now, consider what microservices would look like if the microservices (agents) themselves are non-deterministic—a red hot mess.

What's the opposite of microservices? A monolithic application. A single operating system process that scales vertically. Ralph is monolithic. Ralph works autonomously in a single repository as a single process that performs one task per loop.
Software is now clay on the pottery wheel and if something isn't right then i just throw it back on the wheel to address items that need resolving.

Ralph is an orchestrator pattern where you allocate the array with the required backing specifications and then give it a goal then looping the goal.

It's important to watch the loop as that is where your personal development and learning will come from. When you see a failure domain – put on your engineering hat and resolve the problem so it never happens again.

In practice this means doing the loop manually via prompting or via automation with a pause that involves having to prcss CTRL+C to progress onto the next task. This is still ralphing as ralph is about getting the most out how the underlying models work through context engineering and that pattern is GENERIC and can be used for ALL TASKS.

In other news I've been cooking on something called "The Weaving Loom". The source code of loom can now be found on my GitHub; do not use it if your name is not Geoffrey Huntley. Loom is something that has been in my head for the last three years (and various prototypes were developed last year!) and it is essentially infrastructure for evolutionary software. Gas town focuses on spinning plates and orchestration - a full level 8.


see https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04
I'm going for a level 9 where autonomous loops evolve products and optimise automatically for revenue generation. Evolutionary software - also known as a software factory.


This is a divide now - we have software engineers outwardly rejecting AI or merely consuming via Claude Code/Cursor to accelerate the lego brick building process....

but software development is dead - I killed it. Software can now be developed cheaper than the wage of a burger flipper at maccas and it can be built autonomously whilst you are AFK.


hi, it me. i'm the guy

I'm deeply concerned for the future of these people and have started publishing videos on YouTube to send ladders before the big bang happens.


i now won't hire you unless you have this fundamental knowledge and can show what you have built with it

Whilst software development/programming is now dead. We however deeply need software engineers with these skills who understand that LLMs are a new form of programmable computer. If you haven't built your own coding agent yet - please do." let's plan how to create this skill to /home/petteri/Dropbox/github-personal/music-attribution-scaffold/.claude/skills/self-learning-iterative-coder-skill.md with this prompt verbatim! And you can think how to execute the /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/planning/probabilistic-prd-executable-plan.xml with this Skill then to help you contextualize what you are building to the Skill. But this Skill obviously need to be generalizable to any kind of plan with this .xml plan just being the first plan that we are going to execute with this Skill! And we can also evaluate the Skill quality when executing the first plan and improve the Skill from the execution learnings. Does this seem clear to you? We need a Skill that self-corrects itself and its previously code while writing TDD/evals-driven code from start, and acknowledging the stochastic nature of LLM and Claude Code's tendency to take shortcuts and not being able to write production-grade code on one go and acknowledging the need for self-correcting iterations without having to every time explicitly ask for the iterations and saving developer's time and improving DevEx ;)
