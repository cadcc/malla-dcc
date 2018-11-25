let ramos = document.getElementsByClassName("ramo");


let addOrRequirement = function(reqs) {
    let ids = reqs.split("/");
    for (let i = 0; i < ids.length; i++) {
        console.log(ids[i]);
        let requirement = document.getElementById(ids[i]);
        requirement.classList.add("or")
    }
};

let addSimRequirement = function(req) {
    console.log(req);
    let requirement = document.getElementById(req);
    requirement.classList.add("simul");
};

let addNormalRequirement = function(req) {
    console.log(req);
    let requirement = document.getElementById(req);
    requirement.classList.add("req");
};

let addRequirement = function(req) {
    if (req.includes("/")) {
        addOrRequirement(req);
    } else if(req.slice(-1) === "S") {
        addSimRequirement(req.slice(0, -1));
    } else {
        addNormalRequirement(req);
    }
};

let ramoMouseOver = function() {
    let id = this.getAttribute("id");
    let requirements = JSON.parse(this.getAttribute("data-requirements"));
    for (let i = 0; i < ramos.length; i++) {
        if (ramos[i].id !== id) {
            ramos[i].classList.add("blur");
        }
    }
    for (let i = 0; i < requirements.length; i++) {
        addRequirement(requirements[i]);
    }
};

let ramoMouseOut = function() {
    console.log('out');
    for (let i = 0; i < ramos.length; i++) {
        ramos[i].className = "ramo";
    }
};

for (let i = 0; i < ramos.length; i++) {
    ramos[i].addEventListener('mouseover', ramoMouseOver, false);
    ramos[i].addEventListener('mouseout', ramoMouseOut, false);
}