const navbar = document.querySelector('.nav');
// const navLinks1 = document.getElementById("nav-links-1");
// const navLinks2 = document.getElementById("nav-links-2");
// const navLinks3 = document.getElementById("nav-links-3");
// const navLinks4 = document.getElementById("nav-links-4");


window.addEventListener('scroll', function () 
{
 if (window.pageYOffset > 100) 
 {
 navbar.classList.add('navbar-fixed');
 } 
 else 
 {
 navbar.classList.remove('navbar-fixed');
 }
});

function showpage(index)
{
    const p = document.querySelector('.show-classdemo');
    console.log('p', p);
    switch(index) 
    {
        case 1:
            p.innerHTML = `<iframe src="./ai-experience/w08/w08index.html" width="100%" height="100%" />`
            break;

        case 2:
            p.innerHTML = `<iframe src="./ai-experience/w07/w07index.html" width="100%" height="100%" />`
            break;

        case 3:
            p.innerHTML = `<iframe src="./ai-experience/1111demo/w08/w08LandingPage.html" width="100%" height="100%" />`
            break;
         
        case 4:
            p.innerHTML = `<iframe src="./ai-experience/w03/411770083-陳宜-922-課堂作業.html" width="100%" height="100%" />`
            break;

        case 5:
            p.innerHTML = `<iframe src="./ai-experience/w05/index(1).html" width="100%" height="100%" />`
            break;

        case 6:
            p.innerHTML = `<iframe src="./ai-experience/w06/w06index.html" width="100%" height="100%" />`
            break;

    }
}
// let btn=document.querySelector(".work-resume-btn");
// btn.addEventListener("click", function()
//     {
//         showpage(0)
//     })