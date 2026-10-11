import * as THREE from "three";
import { DRACOLoader, GLTF, GLTFLoader } from "three-stdlib";
import { setCharTimeline, setAllTimeline } from "../../utils/GsapScroll";
import { decryptFile } from "./decrypt";

const setCharacter = (
  renderer: THREE.WebGLRenderer,
  scene: THREE.Scene,
  camera: THREE.PerspectiveCamera
) => {
  const loader = new GLTFLoader();
  const dracoLoader = new DRACOLoader();
  dracoLoader.setDecoderPath("/draco/");
  loader.setDRACOLoader(dracoLoader);

  const loadCharacter = () => {
    return new Promise<GLTF | null>((resolve, reject) => {
      decryptFile("/models/character.enc", "Character3D#@")
        .then((encryptedBlob) => {
          const blobUrl = URL.createObjectURL(new Blob([encryptedBlob]));
          loader.load(
            blobUrl,
            (gltf) => {
              void (async () => {
                const character = gltf.scene;
                await renderer.compileAsync(character, camera, scene);
                character.traverse((child) => {
                  if (!(child instanceof THREE.Mesh)) {
                    return;
                  }
                  child.castShadow = false;
                  child.receiveShadow = false;
                  child.frustumCulled = true;
                  if (child.material && !Array.isArray(child.material)) {
                    (child.material as THREE.ShaderMaterial).precision = "mediump";
                  }
                });
                resolve(gltf);
                setCharTimeline(character, camera);
                setAllTimeline();
                character.getObjectByName("footR")!.position.y = 3.36;
                character.getObjectByName("footL")!.position.y = 3.36;
                dracoLoader.dispose();
                URL.revokeObjectURL(blobUrl);
              })().catch(reject);
            },
            undefined,
            (error) => {
              console.error("Error loading GLTF model:", error);
              reject(error);
            }
          );
        })
        .catch((error) => {
          console.error("Error decrypting character model:", error);
          reject(error);
        });
    });
  };

  return { loadCharacter };
};

export default setCharacter;
