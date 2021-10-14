'use strict';

// 30x20

const Tiles = props => {
    const [tileId, setTileId] = React.useState([10,10])
    const tileArray = [];
    for (let iy = 1; iy<=20; iy+=1 ) {
        for (let ix = 1; ix<=30; ix+=1 ) {
            let xy = ([ix,iy])
            tileArray.push(xy);
    }
    }

    console.log(tileArray)

    const tileDivs = tileArray.map((tileNum) =>
    <img className="tile" key={`[${tileNum[0]},${tileNum[1]}]`} id={`[${tileNum[0]},${tileNum[1]}]`} src="static/img/testbox.jpg"></img>
    )

    return <section className="map">{tileDivs}</section>

}


ReactDOM.render(<Tiles/>, document.querySelector('#container'))