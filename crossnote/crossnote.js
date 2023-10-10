const { Notebook } = require('crossnote');

// console.log(process.argv);
const md_path = process.argv[2];
console.log(md_path);

async function main() {
    const notebook = await Notebook.init({
        notebookPath: 'D:/MyRunProject/Github/markdown-preview-enhanced-for-Windows/crossnote/testCase',
        config: {
            previewTheme: 'github-light.css',
            mathRenderingOption: 'KaTeX',
            codeBlockTheme: 'github.css',
            printBackground: true,
            enableScriptExecution: true, // <= For running code chunks.
        },
    });

    // Get the markdown engine for a specific note file in your notebook.
    const engine = notebook.getNoteMarkdownEngine('离散数学复习重点.md');

    // open in browser
    await engine.openInBrowser({ runAllCodeChunks: true });

    await new Promise(resolve => setTimeout(resolve, 3000));

    return process.exit();
}


main();