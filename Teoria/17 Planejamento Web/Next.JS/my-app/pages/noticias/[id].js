import { useRouter } from 'next/router';

export default function Noticias() {
  const router = useRouter();
  const { id } = router.query;

  return <p>ID da Notícia: {id}</p>;
}