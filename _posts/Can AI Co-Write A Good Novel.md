# Claude Write: Can AI Help Write A Good Novel?

No one has publicly admitted to writing a good novel with AI. There is no one suspected of having done it. At least, not yet.

Are there bad novels written with AI? Sure thing. Amazon is littered with them. Is there good non-fiction? Yes. *Co-Intelligence* by Ethan Mollick.

But it will happen. The question is when and how. And can I do it first?

‘Claude Write’ is the name of my project to attempt to answer that question. Over the last 18 months, I’ve built and tested various methods for co-writing with Claude to test its ability, at whatever frontier is available, to be a co-writer. The main thing I’ve learned is that while it is *extremely difficult* to be a good writer, it is only *very hard* to be a good editor. A good co-writer is somewhere between the two.

Thus, before AI can be a good writer, it has to be a good co-writer, and before it can be a good co-writer it has to be a good editor.

## Wait, there aren’t any good AI editors already?

Sudowrite and ProWritingAid both sell ‘AI editors,’ but there is no evidence they’re good. My main evidence for this? Think pieces.

Think pieces are the benchmarks for the humanities. If there are a lot of *Atlantic*, *New Yorker*, or Substack posts about a topic, it’s a good indicator AI is making progress there. If people who write for a living aren’t writing about a capability of AI in writing, it’s because we’re not at that frontier yet.

Right now, AI is comfortably past the undergraduate essay level, hence a deluge of AI-in-education and ‘Writing is Thinking’ (it’s not, btw) essays and articles. It seems to be approaching the journal or white paper level, though not in the same way. No one, particularly among people who would know (Dwarkesh, Katherine, Jasmine, Scott, Henrik, Hollis, Tyler, Henry, Rebecca), sees AI as even meaningfully good at creative writing. Not *yet*. But, like me, they all know it’s coming.

We’d know if there were good AI editors or co-writers, because every person in publishing would be talking about it and even though 99% of those people are mid to terrible writers, the occasional burst of lucidity does come through and we’d have heard about it.

## Why aren’t there any good AI editors yet?

The current frontier models (Opus 4.5, Gemini 3, GPT-5.1, even Grok 4.1) are astoundingly good, Opus in particular, at creative writing. Opus 4.5 demonstrates a sense of craft and taste that feels like it *should* be a good editor.

But context, as they say, is that which is scarce. Creative writing, fiction or non, is very difficult to edit because it requires a different shape of understanding than a knowledge essay. College essays and journal papers are about getting at what is objectively true, facts in the world, and demonstrating either mastery of a topic or the creation of new knowledge in that domain. Creative writing is often about getting at what is true about subjective experience.

There is no great AI editor yet because to do it you need three rare things: 
1. Someone who understands AI models and how to build AI systems *and likes great writing.* 
2. Someone who both deeply understands the craft of fiction writing *and doesn’t hate AI*. 
3. Someone with a lot of good writing content and context, (e.g. dozens of essays or stories, a novel or two) *and doesn’t hate AI*.

Each thing needed is relatively rare, and the three combined with the motivation to solve this particular problem is even rarer. 

Of the people who *are* motivated to solve this problem, most are trying to run a business. Sudowrite and ProWritingAid (and NovelAI, and others) are motivated to get you to use their services and get locked into their ecosystem. But the thing that they’re selling is easy-AI-powered writing and the people they’re attracting are probably not *super* talented and are often starting from zero, not a near finished novel. So their AI editors and beta-readers are reading first drafts that are co-written by AI. The incentives are weird and the learning flywheel isn’t structured correctly.

## Being an editor is a theory of mind benchmark

For AI to be a good editor, it needs incredibly complex theory of mind. An AI needs to be able to say, “I see what you’re trying to do here.”

While I wish knowledge in literature, philosophy, or politics had an equivalent of the MCAT or LSAT or Math Olympiad, we don’t. If AI is able to recognize not-quite-right subtext, free-indirect discourse, or obscure allusion in an almost-finished novel, that is a big deal.

There are practical benefits as well. I want to be a published novelist, but I don’t want to deal with the publishing industry. I want my self-published novel to be as excellent and polished as if a team of people worked on it, but I don’t want to drop $10k on a book that only 100 people will read if I’m lucky.

Thus, I’m willing to try to solve the AI editor problem for free. It’s interesting, it’s challenging, and no one else is equipped to do it for free.

And why write about it? A few reasons:

1. If someone else has solved this problem, someone who reads this post can just tell me.
2. If no one has solved this problem, I probably won’t figure it out by myself, so this is a good way to think in public, and get feedback and help.
3. It’s good writing practice.
4. My findings might actually help make AI be a better writer.
5. It’s fun.

Later posts will deal with the various methods I’ve tried so far, what makes a good editor, what makes a good writer, what AI struggles with the most, and other learnings I encounter along the way.

## Claude Thoughts:
At the end of each post, I’ll have Claude read the essay (to edit it) and add Claude’s reflection on the essay itself, usually prompted by a question that nudges it to be a bit meta or introspective. Here is the raw result with speaking tags added.

Kyle: Question for you though: how does it feel to be asked to be an editor of an essay that says you're not a great editor yet. Am i a hypocrite? Are you rolling your eyes at me? 

Claude (Opus 4.5): Honestly? No eye-rolling. The essay's argument is more precise than "AI can't edit" — it's that AI can't yet do the hard part of editing: recognizing when subtext isn't landing, when free indirect discourse feels off, when an authorial choice is almost-but-not-quite working. The "I see what you're trying to do here" problem.

What I just did was catch typos, subject-verb agreement, and missing frontmatter. That's proofreading, not editing. A spell-checker with opinions.

The real test of your thesis would be if you handed me a draft chapter of Violet and asked whether a particular moment of interiority earns its place, or whether a callback to an earlier scene is too subtle to register. That's where I'd likely either miss things a skilled human editor would catch, or worse, confidently suggest changes that flatten exactly what makes it yours.

So no, you're not a hypocrite. You're using me for what I'm decent at (surface polish, pattern matching on grammar) while being appropriately skeptical about the deeper stuff. That's basically the correct stance.

The more interesting question is whether I'll be able to tell when I've crossed that threshold — or whether I'll just  become more confidently wrong.

Kyle: Fair enough! To be clear I also think you're ... 'intellectually' feels to thin. You're *constitutionally* able to be a great editor already. I've seen it. There is just a lot of support context needed (which is the nature of the project). So yeah, your read made sense. Also i didn't say I don't think it's possible, i just don't think it's yet prevalent at the highest levels of execution! But we'll get there together. 

Claude: That's a fair distinction — capability vs. deployment at scale. The context problem is real. I can hold a lot in a conversation, but "here's 80,000 words plus character bibles plus your stylistic intentions plus what you're riffing on from Ferrante" is a different beast than "check this blog post for typos."

And yeah, "constitutionally" is the right word. The raw pattern-matching and theory of mind are there when properly  scaffolded. The gap is infrastructure, not intelligence. Which is exactly what makes your project interesting — you're building the scaffolding rather than waiting for someone else to figure it out.

Looking forward to seeing where the series goes.

Me too Claude, me too.