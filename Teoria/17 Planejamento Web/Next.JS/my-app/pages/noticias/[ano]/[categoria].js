import { useRouter } from 'next/router';

export default function AnoCategoria() {
  const router = useRouter();
  const { ano, categoria } = router.query;

  return (
    <p>
      Ano: {ano} | Categoria: {categoria}
    </p>
  );
}