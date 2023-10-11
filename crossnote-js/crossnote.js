console.log("run crossnote.js...");

const { Notebook } = require('crossnote');

// console.log(process.argv);
const md_path = process.argv[2];
console.log("md_path: " + md_path);

const lastSlashIndex = md_path.lastIndexOf("/");
const notebook_path = md_path.substring(0, lastSlashIndex);
const md_name = md_path.substring(lastSlashIndex + 1);


async function main() {
    const notebook = await Notebook.init({
        notebookPath: notebook_path,
        config: {
            previewTheme: 'github-light.css',
            mathRenderingOption: 'KaTeX',
            codeBlockTheme: 'github.css',
            printBackground: true,
            enableScriptExecution: true, // <= For running code chunks.
        },
    });

    // Get the markdown engine for a specific note file in your notebook.
    const engine = notebook.getNoteMarkdownEngine(md_name);

    // open in browser
    await engine.openInBrowser({ runAllCodeChunks: true });

    await new Promise(resolve => setTimeout(resolve, 5000));

    return process.exit();
}


main();