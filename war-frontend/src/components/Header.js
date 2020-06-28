import React, {Component} from "react"
import NavBar from "./Navbar"
import Info from "./Info"

class Header extends Component {

    constructor(props) {
        super(props)
        this.state = {isRoot: false}        
    }

    componentWillMount(props) {
        this.setState(prevState => ({
            isRoot: this.props.isRoot  
        }))
    }
    
    render() {
        const isLoggedin = this.state.isLoggedIn
        return (
            <div className={"header"}>
                <NavBar />
            {this.state.isRoot && <Info />}
             </div>
        )
    }
}

export default Header