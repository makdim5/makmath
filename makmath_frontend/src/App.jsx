import './App.css';
import AuthorizationPage from "./pages/AuthorizationPage/AuthorizationPage";
import HomePage from "./pages/HomePage/HomePage";
import {
    BrowserRouter as Router, Route,
    Routes
} from "react-router-dom";


function App() {
    return (
        <div className="App">

            <Router>

                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/login" element={<AuthorizationPage/>}/>
                </Routes>

            </Router>
        </div>
    );
}

export default App;
