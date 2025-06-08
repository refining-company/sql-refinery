# Todo

Key VS Code Diff Options

🏆 Native Diff Editor (Most Recommended)

- Uses vscode.diff command
- Side-by-side or unified diff view
- Built-in navigation (next/prev change)
- Automatic theme-aware styling
- Same UX as Git diffs, file comparisons
- No custom decoration code needed

👁️ Peek Editor

- Similar to "Go to Definition" peek
- Overlay view without opening new tabs
- Uses editor.action.peekDefinition or custom peek
- Compact, contextual display
- Good for quick comparisons

📍 Inline Decorations (Git-style)

- Red/green gutters like Git blame
- Uses gitDecoration.\* theme colors
- Shows +/- prefixes inline
- Minimal visual disruption
- Good for small changes

🎯 CodeLens Diff Preview

- Clickable lens showing "$(diff) Show changes"
- Expands to show diff inline
- Similar to GitHub's diff expansion
- Non-intrusive until clicked

📝 Hover Diff

- Show diff in hover tooltip
- Uses Markdown with diff syntax highlighting
- Lightweight, contextual
- Good for simple comparisons

Current vs Better Approach:

❌ Current: Custom theme color decorations backgroundColor: new vscode.ThemeColor('diffEditor.removedTextBackground')

✅ Better: Native diff editor vscode.commands.executeCommand('vscode.diff', originalUri, variantUri, 'Title')

Recommendation: Start with Native Diff Editor for the most VS Code-native experience.
