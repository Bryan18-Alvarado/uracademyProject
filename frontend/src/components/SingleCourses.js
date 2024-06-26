import { Link } from "react-router-dom";

function SingleCourse(props) {
  return (
    <div className="col-12 col-md-3 mb-4 d-flex align-items-stretch">
      <div className="card bg-dark w-100">
        <span className="border border-warning"></span>
        <Link to={`/course/${props.course.title}/${props.course.id}`}>
          <img src={props.course.image} className="card-img-top" alt="..." />
        </Link>
        <div className="card-body d-flex flex-column shadow">
          <h4 className="card-title text-center">
            <Link 
              to={`/course/${props.course.title}/${props.course.id}`} 
              style={{ fontFamily: 'ADLaM Display', color: 'white', textDecoration: 'none' }}>
              {props.course.title}
            </Link>
          </h4>
          <h5 className="card-title text-center" style={{ color: 'white' }}>
            Precio: ${props.course.price}
          </h5>
          <div className="mt-auto">
            <button title="Agregar al carrito" className='btn btn-warning btn-sm'>
              <i className="fa-solid fa-cart-arrow-down"></i>
            </button>
            <button title="Agregar a la lista" className='btn btn-danger btn-sm ms-2'>
              <i className="fa fa-heart"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SingleCourse;
