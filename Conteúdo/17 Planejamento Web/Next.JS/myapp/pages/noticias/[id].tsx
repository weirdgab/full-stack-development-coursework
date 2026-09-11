import { useRouter } from 'next/router';
const Noticias = () => {
	const router = useRouter();
	const { id } = router.query;
	return <p>ID da Notícia: {id}</p>;
};

export default Noticias;
