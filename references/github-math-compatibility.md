# GitHub Math Compatibility Contract


GitHub documents support for LaTeX-style expressions in Markdown and says its math capability uses MathJax. It does not publish an exhaustive GitHub-specific macro allowlist. GitHub also preprocesses Markdown before its restricted math component sees the expression. Standard MathJax or LaTeX validity is therefore necessary but not sufficient.

Official references:

- [GitHub Docs: Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
- [GitHub Blog: Math support in Markdown](https://github.blog/news-insights/product-news/math-support-in-markdown/)

The machine-readable authority for this skill is `github-math-compatibility.json`. Its allowed list means only: **these commands passed the recorded GitHub pipeline on the tested date**. It is not a claim about every context, GitHub Enterprise version, or future renderer.

## Verified current subset

The following commands rendered without macro errors in the Continuous Representation Engineering article on August 16, 2026:

`\approx`, `\arctan`, `\begin`, `\cap`, `\cdots`, `\cos`, `\end`, `\frac`, `\in`, `\ldots`, `\left`, `\mathbb`, `\mathrm`, `\mu`, `\ne`, `\phi`, `\pi`, `\qquad`, `\right`, `\sigma`, `\sin`, `\sqrt`, `\sum`, `\text`, `\theta`, `\times`, `\top`, `\varepsilon`, and `\vdots`.

`\quad` was also tested in isolation and survived GitHub Markdown preprocessing. Keep both `\quad` and `\qquad` in the registry, but use spacing only when ordinary mathematical structure cannot communicate the grouping.

## Known recurring failures

### `\operatorname` is forbidden

GitHub's live math component reports `The following macros are not allowed: operatorname`. This first appeared with `\operatorname{SD}` and recurred with `\operatorname{diag}` and `\operatorname{Var}` because the first correction changed only one occurrence.

For short fixed labels, use the tested `\mathrm` form: `\mathrm{SD}`, `\mathrm{diag}`, and `\mathrm{Var}`. Test any more elaborate operator construction instead of inferring compatibility.

### Backslash punctuation is consumed by Markdown

GitHub's Markdown layer converts these TeX spacing commands before the math component receives them:

- `\,` becomes a literal comma;
- `\!` becomes a literal exclamation mark;
- `\;` becomes a literal semicolon;
- `\:` becomes a literal colon.

Do not use them in GitHub-bound Markdown. Prefer ordinary juxtaposition and structural grouping. Do not replace them reflexively with `\cdot`: a centered dot can incorrectly imply an inner product between scalar, vector, or matrix operands.

## Mandatory release gate

For every GitHub-bound document containing mathematics:

1. Run `scripts/check_github_math_compatibility.py <document.md>`. Unknown commands fail closed.
2. For each unknown command, submit an isolated positive and negative control through GitHub's `/markdown` endpoint and its live `math-renderer` element. Capture the final pixels at a relevant viewport.
3. Add a command to the registry only after preprocessing preserves its intended input, the live component produces no macro error, and the rendered operator communicates the right operation.
4. Render the complete clean document through the same pipeline. Require zero “macros are not allowed” messages and zero known preprocessing hazards.
5. Capture at least the most complex changed formula and inspect it visually. Source inspection and DOM text are not substitutes for pixels.
6. When a failure recurs, update the general registry, checker, reference, and regression fixture before fixing the document. A correction that changes only the current occurrence is incomplete.

The compatibility registry grows from observed evidence. Never broaden it from memory or from upstream MathJax documentation alone.
