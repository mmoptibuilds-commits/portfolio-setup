# Plain-English glossary

Use this page when a track uses a word you do not know.

| Term | Plain-English meaning |
|---|---|
| **Repository / repo** | The project folder tracked by Git. |
| **Git** | The system that records versions of your files. |
| **GitHub** | The online service where your Git repository can be stored and shared. |
| **Working tree** | The files currently open on your PC—the version you are editing now. |
| **Branch** | A separate line of work so you can change things without immediately changing `main`. |
| **Commit** | A named saved checkpoint in Git. |
| **Push** | Upload your local commits to GitHub. |
| **Pull** | Download new commits from GitHub into your local copy. |
| **Merge** | Combine one branch into another. |
| **Worktree** | A second physical folder for another Git branch. Useful when two agents must work independently. |
| **CLI** | Command-line interface: a program you control by typing commands in a terminal. |
| **Terminal** | The window where you type PowerShell or CLI commands. |
| **PowerShell** | The Windows command shell used throughout this guide. |
| **Harness** | The program surrounding an AI model and giving it tools. Claude Code, Antigravity and OpenCode are harnesses. |
| **Model** | The AI reasoning engine used inside a harness, such as GLM-5.3 or Gemini 3.1 Pro. |
| **Context** | The information currently visible to the model: prompts, files, tool output and conversation history. |
| **Subagent** | A temporary helper agent given a smaller isolated task. |
| **MCP** | Model Context Protocol: a standard bridge that lets an AI tool connect to another service or tool. |
| **Hook** | A deterministic command that runs when a specific agent event happens, such as before a shell command or after a task. |
| **Frontend** | What a visitor sees and interacts with in the browser. |
| **Backend** | Server-side code that handles private logic, validation and data. |
| **Database** | Structured long-term storage. The production design can use Supabase Postgres. |
| **Authentication / auth** | Proving who a user is. The owner admin area needs auth. |
| **Authorization** | Deciding what an authenticated user is allowed to do. |
| **Environment variable** | A configuration value supplied outside the source code. |
| **Secret** | A private environment value such as an API key. Never commit it to Git. |
| **Domain** | The human-readable name, such as `mmoptibuilds.com`. |
| **DNS** | The records that tell the internet where a domain should go. |
| **Hosting** | The service/computer that actually runs or serves the website. |
| **Deployment** | Publishing a tested build to hosting. |
| **Preview** | A non-production version used to test before affecting the live site. |
| **SEO** | Search-engine optimization: making pages understandable, useful and technically indexable by search engines. |
| **Canonical URL** | The one official URL search engines should treat as the main version of a page. |
| **JSON-LD** | Structured data embedded for search engines; it must describe facts visible on the page. |
| **LCP** | Largest Contentful Paint: how quickly the main visible content loads. |
| **CLS** | Cumulative Layout Shift: how much the page unexpectedly jumps while loading. |
| **INP** | Interaction to Next Paint: how responsive the page feels after user input. |
| **RLS** | Row Level Security: database rules controlling which rows a user may access. |
| **Server Action** | A Next.js function that runs on the server and can handle form submissions. |
| **Idempotent** | Safe to retry without creating duplicate results. |
| **GSAP** | A JavaScript animation library for complex timelines. Use only when simpler CSS cannot express the sequence well. |
| **Lenis** | A smooth-scrolling library. It is optional and must not break keyboard, anchors, reduced motion or performance. |
| **WebGL** | Browser graphics technology used for GPU-rendered 2D/3D scenes. Powerful, but expensive. |
| **Turnstile** | Cloudflare's anti-bot challenge used to protect public forms. |
| **OpenNext** | The adapter currently used by this portfolio to run Next.js on Cloudflare Workers. |
| **vinext** | Cloudflare's currently recommended default path for new Next.js-on-Workers projects. It is not a required migration for this existing portfolio. |

## Next

Go back to the track that sent you here. If you are starting fresh, continue with
[Track 1 — First-time setup](../tracks/01-first-time-setup.md).
