import SellerSideBar from "./SellerSideBar";
import { Link} from 'react-router-dom'
function SellerDashboard(props) {
    return (
        <div className="container mt-4">
            <div className="row">
                <div className="col-md-3 col-12 mb-2">
                    <SellerSideBar />
                </div>
                <div className="col-md-9 col-12 mb-2"> {/* Utilizamos col-md-8 para que ocupe el resto del ancho en dispositivos medianos y más grandes */}
                    <div className="row"> {/* Nueva fila para los elementos internos */}
                        <div className="col-md-4 mb-2">
                            <div className="card shadow ">
                                <div className="card-body text-center">
                                    <h4>Total Course</h4>
                                    <h4><Link to="/">123</Link></h4>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-4 mb-2">
                            <div className="card shadow">
                                <div className="card-body text-center">
                                    <h4>Total Orders</h4>
                                    <h4><Link to="/">123</Link></h4>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-4 mb-2">
                            <div className="card shadow">
                                <div className="card-body text-center">
                                    <h4>Total customer</h4>
                                    <h4><Link to="/">123</Link></h4>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default SellerDashboard;