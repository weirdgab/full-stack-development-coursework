import Link from 'next/link';
import styles from '../styles/Home.module.css';

export default function Home() {
  return (
    <main>
      <h1>Loja Virtual</h1>
      <Link href="/produtos" className={styles.botao}>
        Ver produtos
      </Link>
    </main>
  );
}