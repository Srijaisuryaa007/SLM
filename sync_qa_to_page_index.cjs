const fs = require('fs');
const qaBank = JSON.parse(fs.readFileSync('mobile_app/assets/qa_bank.json', 'utf8'));
const pageIndex = JSON.parse(fs.readFileSync('mobile_app/assets/page_index.json', 'utf8'));

let added = 0;
for (const item of qaBank) {
  const p = item.page.toString();
  if (!pageIndex.pages[p]) {
    pageIndex.pages[p] = {
      unit: `Unit Page ${p}`,
      title: `Book Page ${p}`,
      questions: []
    };
  }
  if (!pageIndex.pages[p].questions) {
    pageIndex.pages[p].questions = [];
  }
  if (!pageIndex.pages[p].questions.includes(item.question)) {
    pageIndex.pages[p].questions.unshift(item.question); // Put verified exercise questions at top!
    added++;
  }
}

fs.writeFileSync('mobile_app/assets/page_index.json', JSON.stringify(pageIndex, null, 2), 'utf8');
console.log(`Synced ${added} high-value questions from qa_bank.json to page_index.json!`);
