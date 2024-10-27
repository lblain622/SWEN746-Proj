export default function Detail({ params }) {
    const { slug } = params;

    return (
        <div>
            <h1>Hello, this is the detail</h1>
            <h2>Slug: {slug}</h2>
        </div>
    );
}