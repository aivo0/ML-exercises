const lava_map1 = [
  "      **               **      ",
  "     ***     D        ***      ",
  "     ***                       ",
  "                      *****    ",
  "           ****      ********  ",
  "           ***          *******",
  " **                      ******",
  "*****             ****     *** ",
  "*****              **          ",
  "***                            ",
  "              **         ******",
  "**            ***       *******",
  "***                      ***** ",
  "                               ",
  "                s              "
];
const lava_map2 = [
  "     **********************    ",
  "   *******   D    **********   ",
  "   *******                     ",
  " ****************    **********",
  "***********          ********  ",
  "            *******************",
  " ********    ******************",
  "********                   ****",
  "*****       ************       ",
  "***               *********    ",
  "*      ******      ************",
  "*****************       *******",
  "***      ****            ***** ",
  "                               ",
  "                s              "
];
const startingPoint = {
  x: 1,
  y: 1
};
const getMapSize = map => ({
  x: map[0].length,
  y: map.length
});
const mapSize = getMapSize(lava_map1);
console.log(getMapSize(lava_map1));
console.log(getMapSize(lava_map2));
const checkStartingPoint = (startingPoint, mapSize) =>
  mapSize.x >= startingPoint.x &&
  startingPoint.x >= 0 &&
  mapSize.y >= startingPoint.y &&
  startingPoint.y >= 0
    ? true
    : false;
console.log(checkStartingPoint(startingPoint, mapSize));
