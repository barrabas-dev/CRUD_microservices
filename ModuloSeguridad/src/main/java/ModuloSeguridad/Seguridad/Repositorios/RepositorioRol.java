package ModuloSeguridad.Seguridad.Repositorios;

import ModuloSeguridad.Seguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioRol extends MongoRepository<Rol,String> {
}