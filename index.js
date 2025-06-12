import fs from 'fs'

var data = JSON.parse(fs.readFileSync('file.json', 'utf8'))
;(() => {
  // console.log(data)
  const item = data.filter((d) => d.colorCode.toLowerCase() === 'af-75')
  console.log(item)
})()
