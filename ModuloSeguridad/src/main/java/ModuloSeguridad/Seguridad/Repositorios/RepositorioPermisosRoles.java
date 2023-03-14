package ModuloSeguridad.Seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import ModuloSeguridad.Seguridad.Modelos.PermisosRoles;


public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
}