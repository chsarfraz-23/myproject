import React, {useState } from 'react';

const App = () => {
    const [name, SetName] = useState('');
    const [price, SetPrice] = useState('');
    const [discount, SetDiscount] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch('http://localhost:8000/myapp/ProductType/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({name, price, discount})
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // Optionally, update UI or state
            })
            .catch(error => console.error('Error:', error));
    };

    return (
        <table className="table table-striped" style={{backgroundColor: "grey", width: "100%"}} >
            <div style={{width: "100%", backgroundColor: "green"}}>
                <h1>Submit Data</h1>
                <form onSubmit={handleSubmit} style={{backgroundColor: "grey"}}>
                    <label>
                        Name:
                        <input type="text" onChange={e => SetName(e.target.value)} value={name}/>
                    </label>
                    <br/>
                    <br/>

                    <label>
                        price:
                        <input type="text" value={price} onChange={(e) => SetPrice(e.target.price)}/>
                    </label>
                    <br/>
                    <br/>
                    <label>
                        Discount:
                        <input type="text" value={discount} onChange={(e) => SetDiscount(e.target.discount)}/>
                    </label>
                    <br/>
                    <br/>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </table>
    )
}
//
//     useEffect(() => {
//         fetch('http://localhost:8000/myapp/ProductType/')
//             .then(response => response.json())
//             .then(data => setData(data))
//             .catch(error => console.error('Error fetching data:', error));
//     }, []);
//     return (
//         <table style={{width: '100%'}}>
//             <div>
//                 <h1>Welcome To My Application </h1>
//                 <ul>
//                     {data.map(item => (
//                         <li key={item.id}>{item.name}: {item.price} : {item.discount}</li>
//                     ))}
//                 </ul>
//             </div>
//         </table>
//     )
// }
export default App;

