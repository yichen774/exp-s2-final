 let x=0;
 cache=""
 function change(){
    x++;
    var newImg = document.createElement('img');
    newImg.src = '252086414-00' + x + '.png';
    document.getElementById('photo-img').src = '/static/images/252086414-00'+x+'.png';
}
function changep(){
    x--;
    var newImg = document.createElement('img');
    newImg.src = '252086414-00' + x + '.png';
    document.getElementById('photo-img').src = '/static/images/252086414-00'+x+'.png';
}