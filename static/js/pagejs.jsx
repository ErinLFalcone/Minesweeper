'use strict';

// 50x38
function SingleTile(props) {
    return <div className="tile" id={props.id}></div>;

}

return ReactDOM.render(<SingleTile id="11" />, document.querySelector('#container'))
