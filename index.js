const fs = require("fs");
const data = require("./build/data.json");
// console.log(data);

let categories = [];
let db = new Object();
let x = 1;
let y = 1;
data.forEach((obj) => {
  if (obj["category"] && categories.indexOf(obj["category"]) === -1) {
    categories.push(obj["category"]);
  }
});
categories.forEach((category) => {
  const categoryStr = category.toString().toLowerCase();
  const routeName = categoryStr.replaceAll(/\s+/g, "-");
  console.log(routeName);
  db[`${category}`] = {
    id: x,
    title: category,
    routeName: routeName,
    items: [],
  };
  x += 1;
});
categories.forEach((category) => {
  data.forEach((obj) => {
    if (obj["category"] === category) {
      db[`${category}`].items.push({
        id: y,
        name: obj["title"],
        imageUrl: obj["imageUrl"],
        price: obj["price"],
      });
      y += 1;
    }
  });
  y = 0;
});
fs.writeFileSync("./build/shop.data.json", JSON.stringify(db));
