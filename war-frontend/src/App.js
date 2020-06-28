import React from "react"
import Header from "./components/Header"
import Footer from "./components/Footer"
import Arena  from "./components/Arena"
function App() {
    return (
        <div>
            <Header isRoot={true}/>
            <Arena />
            <Footer />
        </div>
    )
}

export default App