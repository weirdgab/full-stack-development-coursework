import Link from 'next/link';

function Home() {
	return (
		<ul>
			<li>
				<Link href="/noticias/xpto">
					<a>Vai para pages/noticias/[id].js</a>
				</Link>
			</li>
			<li>
				<Link href="/noticias?ano=2022&categoria=esportes">
					<a>Vai para pages/noticias/[ano]/[categoria].js</a>
				</Link>
			</li>
			<li>
				<Link href="/noticias/2022/esportes">
					<a>Vai para pages/noticias/[ano]/[categoria].js</a>
				</Link>
			</li>
		</ul>
	);
}

export default Home;
