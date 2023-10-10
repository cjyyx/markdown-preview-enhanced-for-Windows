// const program = require('commander');
const { Command } = require('commander')
const program = new Command()

function validator(val) {
    console.log('val', val);
    return val;
}

program
    .version('0.0')
    .option('<md>', 'markdown文件路径，只支持绝对路径', validator)
    .option('--open_in_brower', '在浏览器中打开')
    .option('--output_html [value]', 'output html')
    .parse(process.argv);

console.log(process.argv);
console.log(program.md);
console.log('markdown path: %s', program.md);
