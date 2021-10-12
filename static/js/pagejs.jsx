'use strict';

// 30x20

const pageArray = [];

for (let iy = 1; iy<=20; iy+=1 ) {
    for (let ix = 1; ix<=30; ix+=1 ) {
        let xy = (`[${ix},${iy}]`)
        pageArray.push(xy);
}
}

const tileArray = pageArray.map((tileNum) => 
    <div className="tile" id={tileNum}></div>
)

ReactDOM.render(tileArray, document.querySelector('#container'))

// function SingleTile(props) {
//     return <div className="tile" id={props.id}></div>;

// }

